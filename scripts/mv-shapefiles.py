import sys
import os
import glob
import shapefile
import geopandas as gp
from sqlite3 import dbapi2 as sqlite
import sqlalchemy as sql
from shapely.wkt import dumps as wkt_dumps

#configure sqlite database
eng = sql.create_engine('sqlite:///soil_survey.db', module=sqlite)
conn = eng.connect()

if len(sys.argv) < 2:
	print("./zip-shapefiles.py [dir]")
	exit()

in_dir = sys.argv[1]
target_dir = os.path.abspath(os.path.join(in_dir, "spatial/"))
#print(target_dir)

child_items = os.listdir(target_dir)
child_files = filter(lambda f: os.path.isfile(os.path.join(target_dir, f)), child_items)
distinct_name = set(map(lambda f: os.path.splitext(f)[0], child_files))
distinct_name -= set(['version'])
#print(distinct_name)
for basename in distinct_name:
	shp_path = os.path.join(target_dir, basename + '.shp')
	if not os.path.isfile(shp_path):
		continue

	df = gp.read_file(shp_path)
	df["geometry"] = df["geometry"].apply(wkt_dumps)
	table_name = '_'.join(basename.split('_')[:-1])
	df.to_sql(table_name, conn, if_exists='append', index=False)
