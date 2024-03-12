import pymysql as p

"""
server name -> localhost
username -> root
password -> ''

"""
myobj = p.connect("localhost", "root", "")
cursorobj = myobj.cursor()
try:
    db = "create database school"
    cursorobj.execute(db)
    print("\ndatabase created ")

except:
    print("\nerror!!")


