SELECT movies.title FROM movies WHERE movies.id IN
(SELECT stars.movie_id FROM stars
WHERE stars.person_id IN
(SELECT people.id FROM people
WHERE people.name = "Johnny Depp" OR people.name = "Helena Bonham Carter")
GROUP BY stars.movie_id
HAVING COUNT(*) = 2);