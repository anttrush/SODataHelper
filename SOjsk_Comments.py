import  pymysql
import re

db = pymysql.connect("192.168.3.123","SOjsk","568321","stack_overflow_2017_0831")
cursor = db.cursor()
###
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)

with open("D:\\SOData\\Comments.xml",'r',encoding='utf-8') as f:
    for data in f:
        m = re.match(r'\s+<row Id="(?P<Id>\d+)" PostId="(?P<PostId>\d+)" Score="(?P<Score>\-?\d+)" Text="(?P<Text>.+?)" CreationDate="(?P<CreationDate>[0-9T:\.\-]+)".+?/>\s+', data)
        if m is None:
            print("ERROR: m is None: " + data)
            continue
        comment = m.groupdict()
        # mysql not store 'Text' column
        sql = """INSERT INTO comments(Id,PostId,Score,CreationDate)
                VALUES(%d,%d,%d,"%s")""" % \
                    (int(comment.get("Id")), int(comment.get("PostId")), int(comment.get("Score")), comment.get("CreationDate"), )
        try:
            cursor.execute(sql)
            db.commit()
            print("SQLsuc: " + comment.get("Id"))
        except:
            db.rollback()
            print("SQLfail: " + sql)
db.close()
