SELECT 
    COUNT(transactionID) AS total_transaction,
    date
FROM 
    `data-to-insights.ecommerce.all_sessions`
WHERE 
    transaction_id IS NOT NULL
    AND PARSE_DATE("%Y%m%d", date) >= '2018-01-01'
GROUP BY date 
ORDER BY date DESC
