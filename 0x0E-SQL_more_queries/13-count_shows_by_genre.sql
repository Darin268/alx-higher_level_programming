-- Lists all genres from `hbtn_0d_tvshows` and displays
-- the number of shows linked to each.
SELECT genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
JOIN genres ON tv_show_genres.genre_id = genres.id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY genre
ORDER BY number_of_shows DESC;
