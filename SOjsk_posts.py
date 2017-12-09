import  pymysql
import re

db = pymysql.connect("192.168.3.123","SOjsk","568321","stack_overflow_2017_0831")
cursor = db.cursor()
###
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)

with open("D:\\SOData\\example.xml",'r',encoding='utf-8') as f:
    for data in f:
        m = re.match(r'.+ Id="(\d+)" PostTypeId="(\d+)" .+',data)
        if m:
            PostTypeId = m.group(2)
            if PostTypeId == '1': #question
                # Id,CreationDate,AcceptedAnswerId,Score,ViewCount,Body,Title,Tags,AnswerCount,CommentCount,FavoriteCount
                m = re.match(r'\s+<row Id="(?P<Id>\d+)" PostTypeId="(?P<PostTypeId>1)" (AcceptedAnswerId="(?P<AcceptedAnswerId>\d+)" )?CreationDate="(?P<CreationDate>[0-9T:\.\-]+)" Score="(?P<Score>\-?\d+)" ViewCount="(?P<ViewCount>\d+)" Body="(?P<Body>.+?)" .+?Title="(?P<Title>.+?)" Tags="(?P<Tags>.+?)" AnswerCount="(?P<AnswerCount>\d+)" CommentCount="(?P<CommentCount>\d+)"( FavoriteCount="(?P<FavoriteCount>\d+)")?.+?/>\s+', data)
                if m is None:
                    print("ERROR m is None: " + data)
                    continue
                '''
                m = re.match(r'.+ CreationDate="([0-9T:\.\-]+)" .+', data)
                if m:
                    CreationDate = m.group(1)
                m = re.match(r'.+ AcceptedAnswerId="(\d+)" .+', data)
                if m:
                    AcceptedAnswerId = m.group(1)
                m = re.match(r'.+ Score="(\d+)" .+', data)
                if m:
                    Score = m.group(1)
                m = re.match(r'.+ ViewCount="(\d+)" .+', data)
                if m:
                    ViewCount = m.group(1)
                m = re.match(r'.+ Body="(.+?)" OwnerUserId.+', data)
                if m:
                    Body = m.group(1)
                m = re.match(r'.+ Title="(.+?)" Tags.+', data)
                if m:
                    Title = m.group(1)
                m = re.match(r'.+ Tags="(.+?)" AnswerCount.+', data)
                if m:
                    Tags = m.group(1)
                m = re.match(r'.+ AnswerCount="(\d+)" .+', data)
                if m:
                    AnswerCount = m.group(1)
                m = re.match(r'.+ CommentCount="(\d+)" .+', data)
                if m:
                    CommentCount = m.group(1)
                m = re.match(r'.+ FavoriteCount="(\d+)" .+', data)
                if m:
                    FavoriteCount = m.group(1)
                    '''
                ques = m.groupdict()
                sql = """INSERT INTO questions(Id,CreationDate,AcceptedAnswerId,Score,ViewCount,Body,Title,Tags,AnswerCount,CommentCount,FavoriteCount)
                    VALUES(%d,"%s",%d,%d,%d,"%s","%s","%s",%d,%d,%d)""" % \
                        (int(ques.get("Id")), ques.get("CreationDate"), int(ques.get("AcceptedAnswerId") is None and '0' or ques.get("AcceptedAnswerId")), int(ques.get("Score")), int(ques.get("ViewCount")), ques.get("Body"), ques.get("Title"),ques.get("Tags"),int(ques.get("AnswerCount")),int(ques.get("CommentCount")),int(ques.get("FavoriteCount") is None and '0' or ques.get("FavoriteCount")))
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("SQLsuc: " + ques.get("Id"))
                except:
                    db.rollback()
                    print("SQLfail: " + sql)
            elif PostTypeId == '2': #answer
                m = re.match(r'\s+<row Id="(?P<Id>\d+)" PostTypeId="(?P<PostTypeId>2)" ParentId="(?P<ParentId>\d+)" CreationDate="(?P<CreationDate>[0-9T:\.\-]+)" Score="(?P<Score>\-?\d+)" Body="(?P<Body>.+?)" .+?CommentCount="(?P<CommentCount>\d+)".+?/>\s+',data)
                if m is None:
                    print("ERROR m is None: " + data)
                    continue
                ans = m.groupdict()
                sql = """INSERT INTO answers(Id,CreationDate,ParentId,Score,Body,CommentCount)
                    VALUES(%d,"%s",%d,%d,"%s",%d)""" % \
                      (int(ans.get("Id")), ans.get("CreationDate"), int(ans.get("ParentId")), int(ans.get("Score")), ans.get("Body"), int(ans.get("CommentCount")))
                '''
                m = re.match(r'.+ CreationDate="([0-9T:\.\-]+)" .+', data)
                if m:
                    CreationDate = m.group(1)
                m = re.match(r'.+ ParentID="(\d]+)" .+', data)
                if m:
                    ParentID = m.group(1)
                m = re.match(r'.+ Score="(\d+)" .+', data)
                if m:
                    Score = m.group(1)
                m = re.match(r'.+ Body="(.+?)" OwnerUserId.+', data)
                if m:
                    Body = m.group(1)
                m = re.match(r'.+ CommentCount="(\d+)" .+', data)
                if m:
                    CommentCount = m.group(1)
                sql = """INSERT INTO answers(Id,CreationDate,ParentID,Score,Body,CommentCount)
                                    VALUES(%d,"%s",%d,%d,%s,%d)""" % \
                      (int(Id), CreationDate, int(ParentID), int(Score), Body, int(CommentCount))
                      '''
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("SQLsuc: " + ans.get("Id"))
                except:
                    db.rollback()
                    print("SQLfail: " + sql)
            else: # other type?
                print("TYPE EXCET: Id: "+m.group(1)+" PostTypeId: "+PostTypeId+" \n    data: "+data)
        else: # don't have Id or type?
            print("ID/TYPE ERROR: " + data)
db.close()
