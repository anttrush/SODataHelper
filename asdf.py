with open('/home/jsk/SOdata/Posts.xml','r') as fr:
#with open('D:\\SOData\\example.xml', 'r') as fr:
    fileN = 0
    index = 0
    for line in fr:
        if index == 0:
            fw = open('/home/jsk/SOdata/Posts/P'+str(fileN),'w')
            #fw = open('D:\\SOData\\example\\V'+str(fileN),'w')
            fw.write('<?xml version="1.0" encoding="utf-8"?>\n')
            fw.write('<posts>\n')
        index += 1
        fw.write(line)
        if index == 50000:
            #if index == 2:
            index = 0
            fileN += 1
            fw.write('</posts>')
            fw.close()


