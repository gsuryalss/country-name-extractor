import urllib.request as ur
import json
import mysql.connector


url_ip = "http://country.io/names.json"
resp = ur.urlopen(url_ip).read().decode('utf-8')
print(resp)
count_dat = json.loads(resp)
# count_dat = {"US" : "United States of America"}
# print(len(count_dat))
# for key, value in count_dat.items():
#     print(key, " - ", value)

config = {
    'user': 'root',
    'password': 'rose1234',
    'host': 'localhost',
    'database':'countries01',
    'raise_on_warnings': True,
    'use_pure':False,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

country_table = ( "CREATE TABLE cntry01 ("
                  " `cntry_id` int(3) NOT NULL AUTO_INCREMENT,"
                  " `cntry_code` varchar(6) NOT NULL,"
                  " `cntry_name` varchar(64) NOT NULL,"
                  " PRIMARY KEY (cntry_id)"
                  ") ENGINE=InnoDB")

# creating table
cursor.execute(country_table)

add_countries = ("INSERT INTO cntry01"
                 "(`cntry_code`, `cntry_name`) "
                 "VALUES (%s, %s)")

for key, val in count_dat.items():
    data_countries = (key, val)
    cursor.execute(add_countries, data_countries)

cnx.commit()
cursor.close()
cnx.close()

