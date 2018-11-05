IFS=$'\n'

for table in $(mdb-tables -d, $1 | tr ',' '\n')
do
    mdb-schema -T $table $1;
done
