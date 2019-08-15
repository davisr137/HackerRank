SELECT *
FROM
(
    SELECT Hackers.hacker_id, Hackers.name, SUM(SubChallenge.max_score) AS score
    FROM Hackers
    INNER JOIN 
    (
        SELECT hacker_id, challenge_id, MAX(score) as max_score
        FROM Submissions
        GROUP BY hacker_id, challenge_id
    ) SubChallenge
    ON SubChallenge.hacker_id = Hackers.hacker_id
    GROUP BY Hackers.name, Hackers.hacker_id
    ORDER BY SUM(SubChallenge.max_score) DESC, Hackers.hacker_id ASC
) T
WHERE T.score > 0
