CREATE TABLE mydataset.myclusteredtabe
(
    c1 NUMERIC,
    userID STRING,
    c3 STRING,
    eventDate TIMESTAMP,
    c5 GEOGRAPHY
)
PARTITION BY DATE(eventDate)
CLUSTER BY userID
OPTIONS (
    partition_expiration_days = 3,
    description='cluster')
AS SELECT * FROM mydataset.myothertable