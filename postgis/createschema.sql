SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;

DROP TABLE if exists massgis_assessor;
DROP TABLE if exists massgis_taxpar;
DROP INDEX if exists massgis_taxpar_loc_id;
DROP INDEX if exists massgis_taxpar_the_geom;
DROP INDEX if exists massgis_assessor_loc_id;

BEGIN;

CREATE TABLE massgis_taxpar (gid serial PRIMARY KEY,
shape_leng numeric,
shape_area numeric,
map_par_id text,
loc_id text,
poly_type text,
map_no text,
source text,
plan_id text,
last_edit int4,
bnd_chk text,
no_match text,
town_id int2,
/* The following are extra fields that are in just one towns files  */
loc_id_isl text,
objectid text,
poly__desc text,
sourc_desc text,
bnd_c_desc text,
no_ma_desc text
);

SELECT AddGeometryColumn('','massgis_taxpar','the_geom',900913,'MULTIPOLYGON',2);

CREATE TABLE "massgis_assessor" (gid serial PRIMARY KEY,
"prop_id" text,
"loc_id" text,
"bldg_val" int4,
"land_val" int4,
"other_val" int4,
"total_val" int4,
"fy" int2,
"lot_size" numeric,
"ls_date" text,
"ls_price" int4,
"use_code" text,
"site_addr" text,
"addr_num" text,
"full_str" text,
"location" text,
"city" text,
"zip" text,
"owner1" text,
"own_addr" text,
"own_city" text,
"own_state" text,
"own_zip" text,
"own_co" text,
"ls_book" text,
"ls_page" text,
"reg_id" text,
"zoning" text,
"year_built" int2,
"bld_area" int4,
"units" int2,
"res_area" int4,
"style" text,
"stories" text,
"num_rooms" int2,
"town_id" int2,
"lot_units" text,
/* extra fields in one file */
"objectid" text,
"cama_id" text,
"loc_id_isl" text
);

CREATE INDEX massgis_taxpar_loc_id ON massgis_taxpar (loc_id);
CREATE INDEX massgis_taxpar_the_geom ON massgis_taxpar using GIST (the_geom);
CREATE INDEX massgis_assessor_loc_id ON massgis_assessor (loc_id);


COMMIT;

