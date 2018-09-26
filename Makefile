data/%: data/%.zip
	unzip data/%.zip

data/%.zip: url-list.txt data
	wget -nc -i $< -P data

data:
	mkdir data

db/soil_survey.db:
	sqlite3 $@ < db/schema.txt
