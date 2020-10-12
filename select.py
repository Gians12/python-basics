import psycopg2
#connection args
dbname="dbname="
user="user= "
password="password= "
host="host= "
#enter args
dbname+="'name'"
user+="'user1'"
password+="'********'"
host+="'host1'"
##########################
args= dbname+user+password+host
#establish Query
query='select * from cars where car_id<10;'#raw_input("Insert the Query you wanna execute:\t")

def connectDB(args,query):
    try:
        conn=psycopg2.connect(args)
        cur=conn.cursor()
        cur.execute(query)
        rows=cur.fetchall()
        return rows
    except:
        print ("Error1")
        exit()
        
if __name__=="__main__": 
    d=connectDB(args,query)

    try:
        with open('a.txt', 'a') as fp:
            fp.write(' '.join('%s' % i for i in d)+'\n')
        print ("Done!")
    except:
        print ("Error2")
        exit()
