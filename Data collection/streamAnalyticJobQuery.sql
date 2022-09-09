SELECT
    Ident,
    ServerTimestamp,
    PositionDirection,
    PositionLatitude,
    PositionLongitude,
	PositionAltitude,
    PositionSpeed,
    COUNT(*) OVER (PARTITION BY Ident LIMIT DURATION (minute, 1)) 
INTO
    [database]
FROM
    [myIoTInput] 