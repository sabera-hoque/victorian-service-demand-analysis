-- SQLite-compatible examples
-- Load the CSV into a table named service_demand using your preferred SQL client.

-- 1. Monthly demand and completion
SELECT
    month,
    SUM(requests_received) AS total_received,
    SUM(requests_completed) AS total_completed,
    ROUND(100.0 * SUM(requests_completed) / NULLIF(SUM(requests_received), 0), 1)
        AS completion_rate_pct
FROM service_demand
GROUP BY month
ORDER BY month;

-- 2. Regional comparison
SELECT
    region,
    SUM(requests_received) AS total_received,
    SUM(requests_completed) AS total_completed,
    ROUND(100.0 * SUM(requests_completed) / NULLIF(SUM(requests_received), 0), 1)
        AS completion_rate_pct,
    ROUND(AVG(open_requests_end_month), 1) AS avg_open_requests,
    ROUND(AVG(median_wait_days), 1) AS avg_median_wait_days
FROM service_demand
GROUP BY region
ORDER BY avg_open_requests DESC;

-- 3. Flag region-months for review (illustrative thresholds only)
SELECT
    month, region, requests_received, requests_completed,
    open_requests_end_month, median_wait_days
FROM service_demand
WHERE median_wait_days > 30
   OR overdue_requests > 50
ORDER BY month, region;

-- 4. Check duplicate region-month records
SELECT month, region, COUNT(*) AS row_count
FROM service_demand
GROUP BY month, region
HAVING COUNT(*) > 1;
