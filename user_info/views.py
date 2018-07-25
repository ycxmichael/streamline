from django.shortcuts import render
from django.shortcuts import redirect
from global_var_and_func import LISTENER_USERID, sql_update_cmd,sql_fetchone_cmd,sql_fetchall_cmd

# Create your views here.


def user_info(request, user_id):
    context = {'user_id': user_id}
    return render(request, 'user_info/user_info.html', context)

def display_playlist(request, user_id):
    #3. JOIN QUERY:Output playlist name, and all song-related info for user logged in
    #result returns:playlistname, songname, stagename, albumname, tracklength
    get_playlist_sql = "SELECT PIS.playlistname, PIS.songname, AID.stagename, A.albumname, CS.tracklength \
                    FROM playlistincludessongs PIS \
                    JOIN containsong CS ON CS.albumid = PIS.albumid AND CS.songname = PIS.songname \
                    JOIN Album A ON A.albumid = CS.albumid \
                    JOIN createalbum CA ON CA.albumid = A.albumid\
                    JOIN ArtistUserId AID ON AID.userid = CA.userid\
                    WHERE PIS.userid = {};".format(user_id)

    #Find total number of songs in the user playlist
    get_song_count = "SELECT COUNT(*) \
                        FROM playlistincludessongs PIS \
                        JOIN CreatePlaylist CP ON \
    	                PIS.UserID = CP.UserID AND \
    	                PIS.PlaylistName = CP.PlaylistName \
                        JOIN ListenerUserID LID ON CP.UserID = LID.UserID \
                        WHERE PIS.UserID = {}".format(user_id)

    user_playlist = sql_fetchall_cmd(get_playlist_sql)
    total_song_count_playlist = sql_fetchone_cmd(get_song_count)
    #the 'user_id' gets passed to the template
    context = {'user_id': user_id,
                'result': user_playlist,
                'song_count': total_song_count_playlist
               }
    return render(request, 'user_info/playlist.html', context)

def detail(request, user_id):

    if "select_detail" in request.POST:
        selected_value = request.POST["select_detail"]

        context = {'user_id': user_id,
                   'selected_value': selected_value}

        get_user_sql = "SELECT {} FROM {} " \
                       "WHERE UserId = {};".format(selected_value, LISTENER_USERID, user_id)
        print(get_user_sql)
        result = sql_fetchone_cmd(get_user_sql)
        response = result[0]

        if selected_value == 'email':
            context['email'] = response
        elif selected_value == 'firstname':
            context['firstname'] = response
        elif selected_value == 'lastname':
            context['lastname'] = response
        elif selected_value == 'age':
            context['age'] = response

        return render(request, 'user_info/detail.html', context)

    else:
        selected_value = None

    return render(request, 'user_info/detail.html', {'selected_value': selected_value,'user_id': user_id})


def update_age(request, user_id):
    if request.method == 'POST':
        print("I got here")
        age = request.POST.get('new_age', None)
        if age != '':
            update_age_sql = "UPDATE {} SET Age={} WHERE UserId={};".format(LISTENER_USERID, age, user_id)
            print(update_age_sql)
            sql_update_cmd(update_age_sql)
            return redirect("/user_info/" + str(user_id) + "/detail/")

    context = {'user_id' : user_id}
    return render(request, 'user_info/update.html', context)
