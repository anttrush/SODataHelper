import pymysql
import sys

db = pymysql.connect("192.168.7.129","jisk","jisk","stackoverflow")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)

queIdList = [4,13,37296,155669,255302,329652,404299,499834,598931,703538,809664,933165,1066710,1215416,1359973,1501278,1655982,1823254,1987528,2173944,2353219,2557314,2748310,2946565,3154283,3380239,3614080,3835658,4065863,4319979,4572753,4857553,5149047,5507822,5845428,6194884,6542342,6893165,7264841,7617199,7961129,8334833,8691144,9088892,9508667,9960765,10392029,10842808,11278587,11750763,12223786,12666178,13169131,13654917,14106912,14637412,15148028,15735974,16310829,16867653,17395966,17983034,18553933,19105811,19718698,20307139,20864411,21492326,22108106,22774433,23400092,23975562,24500657,25070848,25597364,26132148,26685022,27219813,27727385,28257970,28788450,29380591,29979738,30563959,31150492,31756872,32321631,32877448,33457887,34010297,34552550,35121084,35712223,36345846,36961562,37557444,38135059,38689419,39260778]

lenth = len(queIdList)
print("lenth: " + str(lenth))
adder = 0
#for Id in range(1,121784):
for Id in [100570,115813]:
    sql = "SELECT TagName from stackoverflow.tags where Id=" + str(Id)
    try:
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        tagName = results[0][0]
        print("Id: " + str(Id) + "TagName: " + tagName + ": ")
        adder += 1
    except:
        db.rollback()
        print("getting tag...")
        continue
    #tagName = 'javascript'
    for i in range(0,lenth-1):
       #sql = "SELECT COUNT(*),SUM(Score), SUM(Score+AnswerCount+CommentCount) FROM stackoverflow.questions where Id >= " + str(queIdList[i]) + " and Id < " + str(queIdList[i+1]) + " and Tags like \"%"+ tagName +"%\";"
       sql = "SELECT SUM(Score+AnswerCount+CommentCount) FROM stackoverflow.questions where Id >= " + str(queIdList[i]) + " and Id < " + str(queIdList[i + 1]) + " and Tags like \"%" + tagName + "%\";"

       try:
           cursor.execute(sql)
           db.commit()
           results = cursor.fetchall()
           #print(str(results[0][0]) + "\t" + str(results[0][1]) + "\t" + str(results[0][2]))
           print(str(results[0][0]))
       except:
           db.rollback()
           print("fail:" + sql)
    if (adder >> 2) << 2 == adder:
        pause = sys.stdin.readline()
db.close()
