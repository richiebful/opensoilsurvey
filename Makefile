data/%: data/%.zip
	unzip data/%.zip

data/%.zip: url-list.txt
	wget -nc -i $< -P data

db/soil_survey.db: db/schema.txt
	sqlite3 $@ < $<
