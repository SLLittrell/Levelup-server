SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;
SELECT * FROM levelupapi_game;
SELECT * FROM levelupapi_event;
SELECT * FROM levelupapi_attendee;

SELECT
    e.id,
    e.date,
    e.time,
    g.title,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_event e
JOIN
    levelupapi_game g ON g.id = e.game_id
JOIN
    levelupapi_gamer gr ON gr.id = e.organizer_id 
JOIN
    auth_user u ON gr.user_id = u.id
