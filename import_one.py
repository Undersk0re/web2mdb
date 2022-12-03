import requests
from pprint import pprint
from lxml import html
from pymongo import MongoClient
import html_to_json

link= "https://www.write_where_some_webp.html" #


# access or create new if not exists
DBNAME="GnL"
Collection_name="WebpSites"


Access_string="mongodb://localhost:27017/" # standard
myclient_conn = MongoClient(Access_string)
html_string = requests.get(u1).text ## we can add some regex for a utf ascii filter
d = html_to_json.convert(html_string)
mob = myclient_conn[DBNAME][Collection_name].insert_one(d)


# print json (Optional)
for i in myclient_conn[DBNAME][Collection_name].find():
  pprint (i)
