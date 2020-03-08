SELECT
  title,
  SUM(views) AS sumViews
FROM
  `fh-bigquery.wikipedia_v2.pageviews_2018`
WHERE
  datehour >= "2018-01-01"
  AND wiki IN ("en",
    "en.m")
  AND REGEXP_CONTAINS(title, "G.*o.*o.*g.*")
GROUP BY
  title
ORDER BY
  sumViews DESC