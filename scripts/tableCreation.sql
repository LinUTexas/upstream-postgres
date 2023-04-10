-- public.station definition

-- Drop table

DROP TABLE public.station cascade;
DROP TABLE public.sensor cascade;
drop table campaign cascade;
 DROP TABLE public.sensorobject cascade;
 DROP TABLE public.measurement cascade;



create TABLE public.station (
	stationid serial PRIMARY Key,
	stationname varchar NULL,
	projectid varchar NULL,
	description varchar NULL,
	contactname varchar NULL,
	contactemail varchar NULL,
	active bool NULL,
	startdate timestamp NULL,
	datetime timestamp NULL
);


CREATE TABLE public.campaign (
	campaignid serial PRIMARY KEY, 
	stationid int,
	campaign_description varchar, 
	StartDate timestamp, 
	EndDate timestamp, 
	CONSTRAINT fk_station
      FOREIGN KEY(stationid) 
	  REFERENCES STATION(stationid)
);

-- public.sensor definition

-- Drop table



CREATE TABLE public.sensor (
	sensorid serial PRIMARY Key,
	stationid int NULL,
	sensortype varchar NULL,
	datetype varchar NULL,
	postprocess bool NULL,
	postprocessscript varchar NULL,
	units varchar NULL,
	CONSTRAINT fk_station
      FOREIGN KEY(stationid) 
	  REFERENCES station(stationid)

);

-- public.measurement definition

-- Drop table


CREATE TABLE public.measurement (
	measurementid serial PRIMARY Key,
	sensorid int NULL,
	variablename varchar NULL,
	collectiontime timestamp NULL,
	variabletype varchar NULL,
	elevation float4 NULL,
	measurementvalue float4 NULL,
	CONSTRAINT fk_sensor
      FOREIGN KEY(sensorid) 
	  REFERENCES sensor(sensorid)
);

SELECT AddGeometryColumn ('public','measurement','geometry',4326,'POINT',2);



-- public."object" definition

-- Drop table


CREATE TABLE public.sensorobject (
	objectid serial PRIMARY Key,
	sensorid int NULL,
	filename varchar NULL,
	filetype varchar NULL,
	filesize float4 NULL,
	creationdate varchar NULL,
	geometry point NULL,
	checksum varchar null,
	CONSTRAINT fk_sensor
      FOREIGN KEY(sensorid) 
	  REFERENCES sensor(sensorid)

);



-- grant proper permissions

grant usage on schema public to sensor_user;
grant all on public.sensor to sensor_user;
grant update  on   public.station to sensor_user;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO anon;
grant usage on schema public to sensor_user;
grant all on public.station to sensor_user;
grant usage, select on sequence public.measurement_measurementid_seq to sensor_user;
grant usage, select on sequence public.sensor_sensorid_seq to sensor_user;
grant usage, select on sequence public.station_stationid_seq to sensor_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to sensor_user;