from sqlite3 import dbapi2 as sqlite
import sqlalchemy as sql
import pandas as pd
import sys
import os

#set up database connection
eng = sql.create_engine('sqlite:///soil_survey.db', module=sqlite)
conn = eng.connect()

if len(sys.argv) < 2:
        print("./zip-tabular.py [dir]")
        exit()

in_dir = sys.argv[1]
target_dir = os.path.abspath(os.path.join(in_dir, "tabular/"))

child_items = os.listdir(target_dir)
child_items = map(lambda f: os.path.join(target_dir, f), child_items)
child_files = filter(lambda f: os.path.isfile(f), child_items)

for file_path in child_files:
	df = pd.read_csv(file_path, sep='|', header=None, quotechar='"')
	print(df)
	table_name = os.path.splitext(os.path.basename(file_path))[0]
	print(table_name)
	df.to_sql(table_name, conn, if_exists='append', index=False)
