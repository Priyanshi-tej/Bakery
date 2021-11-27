import pymysql as mysql
def connection():
    db=mysql.connect(host='localhost', port=3306, user="root", password='admin',db='bakery')
    cmd=db.cursor()
    return db,cmd