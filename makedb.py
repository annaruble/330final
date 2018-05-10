import psycopg2, records
db2 = records.Database('sqlite:///dbex/mydb.db')
infile = open('dbex/cdata/city.csv','r')
n = 0
for line in infile:
    if n == 0 :
        n +=1
    elif line[0] == '(':
        pass
    else:
        data = line.rstrip().split('|')
        db2.query("""insert into city values({}, '{}', '{}', '{}', {})""".format(int(data[0]),data[1],data[2],data[3],int(data[4])))


res = db2.query("""select * from city""")
print(res[10])