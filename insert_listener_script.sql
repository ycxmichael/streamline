DELETE FROM ListenerUserID;
DELETE FROM ListenerEmail;

-- INSERT VALUES
INSERT INTO ListenerUserID (UserID,Email,FirstName,LastName,Age)
VALUES
(6, 'dog@dog.com', 'John', 'Doe', 23),
(7,	'mouse@mouse.com', 'Mary', 'Jane', 15),
(8,	'lion@lion.com', 'Simon', 'Smith', 7),
(9, 'cat@cat.com', 'Neko', 'Kawaii', 14),
(10, 'jesus@holywater.com',	'Jesus', 'Christ',2018)
;

INSERT INTO ListenerEmail (Email, Password)
VALUES
('dog@dog.com', '12345'),
('mouse@mouse.com', 'iluvyou'),
('lion@lion.com', '11111'),
('cat@cat.com', '12345'),
('jesus@holywater.com', 'qwerty')
;