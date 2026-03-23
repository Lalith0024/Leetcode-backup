SELECT u.name,
       SUM(t.amount) AS Balance
FROM users u
JOIN transactions t USING (account)
GROUP BY account
HAVING SUM(t.amount) > 10000;
