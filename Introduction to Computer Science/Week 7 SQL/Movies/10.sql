/*
Select movies with rating >= 9.0
Select Directors who has movie.id of movie
Return name of directors
*/
SELECT people.name FROM people WHERE people.id IN
(SELECT directors.person_id FROM directors WHERE directors.movie_id IN
(SELECT movies.id FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE rating >= 9.0));
