from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")

db = client.althoff_auftragsanalyse_db

coll_employees = db["employees"]
coll_work_month = db["work_month"]
coll_orders = db["orders"]