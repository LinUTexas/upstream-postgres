-- public.measurement definition

-- Drop table

 DROP TABLE public.measurement;

CREATE TABLE public.measurement (
	measurementid serial,
	sensorid int NULL,
	variablename varchar NULL,
	collectiontime timestamp NULL,
	variabletype varchar NULL,
	Geometry point NULL,
	elevation float4 NULL,
	measurementvalue float4 NULL
);

-- public.station definition

-- Drop table

DROP TABLE public.station;

CREATE TABLE public.station (
	stationid serial,
	stationname varchar NULL,
	projectid varchar NULL,
	description varchar NULL,
	contactname varchar NULL,
	contactemail varchar NULL,
	active1char bool NULL,
	startdate timestamp NULL,
	datetime timestamp NULL
);

-- public.sensor definition

-- Drop table

DROP TABLE public.sensor;

CREATE TABLE public.sensor (
	sensorid serial,
	stationid int NULL,
	sensortype varchar NULL,
	datetype varchar NULL,
	postprocess bool NULL,
	postprogressscript varchar NULL,
	units varchar NULL
);

-- public."object" definition

-- Drop table

 DROP TABLE public."object";

CREATE TABLE public.sensorobject (
	objectid serial,
	sensorid int NULL,
	filename varchar NULL,
	filetype varchar NULL,
	filesize float4 NULL,
	creationdate varchar NULL,
	geometry point NULL,
	checksum varchar NULL
);