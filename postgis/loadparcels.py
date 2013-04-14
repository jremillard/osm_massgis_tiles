#!usr/bin/python

# Jason Remillard - This file is in the public domain.

import sys, os, zipfile, glob

os.system("rm loadparcel_log.txt");

os.system("psql -q gis -f createschema.sql >> loadparcel_log.txt")

for file in glob.glob("../srcdata/massgis_parcels/*TaxPar.shp") :
  os.system("rm temp/temp*")

  print "parcel " + file + " ",
  os.system("echo parcel " + file + " >> loadparcel_log.txt");

  # reproject to 900913, which is what we use inside of postGIS
  os.system("ogr2ogr -t_srs EPSG:900913 -overwrite temp/temp.shp " + file + " >> loadparcel_log.txt")


  if ( os.system("shp2pgsql -D -s 900913 -a temp/temp.shp massgis_taxpar > temp/massgis_taxpar.sql 2>> loadparcel_log.txt") or 
       os.system("psql -q gis -f temp/massgis_taxpar.sql 2>> loadparcel_log.txt") ) :
    print "FAIL"
  else :
    print "OK"

for file in glob.glob("../srcdata/massgis_parcels/*Assess.dbf") :

  print "assessor " + file + " ",
  os.system("echo assessor " + file + " >> loadparcel_log.txt");

  if ( os.system("shp2pgsql -D -n -a " + file + " massgis_assessor > temp/assessor.sql 2>> loadparcel_log.txt") or 
       os.system("psql -q gis -f temp/assessor.sql >> loadparcel_log.txt")) :
    print "FAIL"
  else :
    print "OK"




