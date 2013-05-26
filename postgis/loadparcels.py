#!/usr/bin/python

# Jason Remillard - This file is in the public domain.

import sys, os, glob

database = "gis"
logfile = "loadparcels_log.txt"

# supply database name on command line if not gis
if ( len(sys.argv) > 1 ) :
  database = sys.argv[1]

os.system("mkdir -p temp")
os.system("rm " + logfile);

os.system("psql -q " + database + " -f createschema.sql >> " + logfile)

for file in glob.glob("../srcdata/massgis_parcels/*TaxPar.shp") :
  os.system("rm temp/temp*")

  os.system("echo parcel " + file + " >> " + logfile)

  # reproject to 900913, which is what we use inside of postGIS, convert to sql, then load
  if ( os.system("ogr2ogr -t_srs EPSG:900913 temp/temp.shp " + file + " >> " + logfile)) :
    print "reproject shape " + file + " FAIL"
  elif ( os.system("shp2pgsql -D -s 900913 -a temp/temp.shp massgis_taxpar > temp/massgis_taxpar.sql 2>> " + logfile)) :
    print "shape convert to sql " + file + " FAIL"
  elif (os.system("psql -q " + database + " -f temp/massgis_taxpar.sql 2>> " + logfile)) :
    print "shape load into pgsql " + file + " FAIL"

for file in glob.glob("../srcdata/massgis_parcels/*Assess.dbf") :
  os.system("echo assessor " + file + " >> " + logfile);

  # convert assessor (aka address data) to sql and load
  if ( os.system("shp2pgsql -W \"latin1\" -D -n -a " + file + " massgis_assessor > temp/assessor.sql 2>> " + logfile)) :
    print "assessor convert to sql " + file + " FAIL"
  elif (os.system("psql -q " + database + " -f temp/assessor.sql >> " + logfile)) :
    print "assessor load into pgsql " + file + " FAIL"




