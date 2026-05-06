create SCHEMA airline;

create table airline.airports_dim (
    airport_id BIGINT,
    city VARCHAR(100),
    state VARCHAR(100),
    name VARCHAR(200)
);


COPY airline.airports_dim
FROM 's3://airline-project-bucket/airport-data/airports.csv'
IAM_ROLE 'arn:aws:iam::025066280149:role/Redshift-Access'
DELIMITER ','
IGNOREHEADER 1
REGION 'us-east-1';

select * from airline.airports_dim limit 5;

create table airline.flights_fact(
    carrier VARCHAR(10),
    dep_airport VARCHAR(200),
    arr_airport VARCHAR(200),
    dep_city VARCHAR(100),
    arr_city VARCHAR(100),
    dep_state VARCHAR(100),
    arr_state VARCHAR(100),
    dep_delay BIGINT,
    arr_delay BIGINT
);

select * from airline.flights_fact LIMIT 5;