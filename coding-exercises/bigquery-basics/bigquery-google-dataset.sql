SELECT
  LANGUAGE,
  title,
  SUM(Views) AS views
FROM
  `bigquery-samples.wikipedia_benchmark.Wiki10B`
WHERE
  title LIKE %Google%
GROUP BY
  LANGUAGE,
  title
ORDER BY
  views DESC;