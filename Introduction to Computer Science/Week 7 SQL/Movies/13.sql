SELECT people.name FROM people WHERE people.id IN
(SELECT DISTINCT(stars.person_id) FROM stars WHERE stars.movie_id IN
(SELECT stars.movie_id FROM stars WHERE person_id IN
(SELECT people.id FROM people
WHERE people.name = "Kevin Bacon" AND people.birth = 1958)))
AND NOT people.name = "Kevin Bacon";

