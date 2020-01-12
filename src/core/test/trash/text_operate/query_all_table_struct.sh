databases=`hive -S -e 'show databases;'`
#for i in `echo $databases`
#do 
#  echo $i 
#done
for database in ${databases}
do
   echo "DB:${database}" >> table_struct.txt
   tables=`hive -S -e "show tables in ${database}"`
   for table in ${tables}
   do
       struct=`hive -S -e "desc ${database}.${table}"`
       echo "table:${table}" >> table_struct.txt
       echo "${struct}" | grep -v "^#" | grep -v "^\s" >> table_struct.txt
       echo "" >> table_struct.txt
   done
done
