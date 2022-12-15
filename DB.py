import pymysql

conn = pymysql.connect(host="localhost", user="root", password="jiwi1234", db="candidseed", charset="utf8")
curs = conn.cursor()

def beforeedit(email, title):
    sql = """select * from wikitext where title='{0}'""".format(title)
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        a = "{0} {1}".format(row[6], email)
        sql = """UPDATE userinfo SET edituser={0} WHERE email='{1}';""".format(a, email)
        curs.execute(sql)
        conn.commit()

def addeditcount(email):
    sql = """select * from userinfo where email='{0}'""".format(email)
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        result = int(row[6] + 1)
        sql = """UPDATE userinfo SET editcounter={0} WHERE email='{1}';""".format(result, email)
        curs.execute(sql)
        conn.commit()
        print ("편집횟수를 추가했습니다.")
        return True

def bringcounter(email):
    sql = """select * from userinfo where email=%s"""
    curs.execute(sql, email)
    rows = curs.fetchall()
    for row in rows:
        return row[6]

def bringcreatetime(email):
    sql = """select * from userinfo where email=%s"""
    curs.execute(sql, email)
    rows = curs.fetchall()
    for row in rows:
        return row[5]

def setuserrank(email, rank):
    beforerank = checkuserrank(email)
    sql = """UPDATE userinfo SET userrank='{0} {1}' WHERE email='{2}';""".format(beforerank, rank, email)
    curs.execute(sql)
    print ("유저권한 변경완료!")
    conn.commit()
    return True

def bringrecent():
    sql = """select * from recentchange WHERE ID<100"""
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    return True

def dbremovetext(title):
    sql = """DELETE FROM wikitext WHERE title = %s;"""
    curs.execute(sql, title)
    conn.commit()
    return True

def numberset(table, text):
    sql = """SET @CNT =0;"""
    curs.execute(sql)
    sql = """UPDATE {0} SET {0}.{1} = @CNT:=@CNT+1;""".format(table, text)
    curs.execute(sql)
    conn.commit()
    return True

def bringemail(email):
    sql = """select * from userinfo where email=%s"""
    curs.execute(sql, email)
    rows = curs.fetchall()
    for row in rows:
        return row[1]

def bringpassword(email):
    sql = """select * from userinfo where email=%s"""
    curs.execute(sql, email)
    rows = curs.fetchall()
    for row in rows:
        return row[2]

def createacc(nik, email, pwd):
    sql = """insert into userinfo(email, password, nickname, userrank, createtime)
            values (%s, %s, %s, 'user', now())"""
    curs.execute(sql, (email, pwd, nik))
    conn.commit()
    return True

def checklogin(email, pwd):
    sql = """select * from userinfo where email=%s"""
    curs.execute(sql, email)
    rows = curs.fetchall()
    for row in rows:
        checkpassward = row[2]  
        if(checkpassward == pwd):
            return row[2]
        else:
            return True

def checkuserrank(email):
    sql = """select * from userinfo where email=%s"""
    curs.execute(sql, email)
    rows = curs.fetchall()
    for row in rows:
        return row[4]

def createtext(pagename):
    sql = """insert into wikitext(text, title, editnumber, createtime)
            values ("여기에 문구를 추가하세요!", %s, 1, now())"""
    curs.execute(sql, pagename)
    conn.commit()
    return True

def checktext(pagename):
    sql = """select * from wikitext where title=%s"""
    curs.execute(sql, pagename)
    rows = curs.fetchall()
    for row in rows:
        print(row[1])
        return row[1]

def checktitle(pagename):
    sql = """select * from wikitext where title=%s"""
    curs.execute(sql, pagename)
    rows = curs.fetchall()
    for row in rows:
        print(row[1])
        return row[1]

def changetext(text, pagename, count):
    sql = """select * from wikitext where title=%s"""
    curs.execute(sql, pagename)
    rows = curs.fetchall()
    for row in rows:
        abc = int(row[3])
        result = abc + 1
        sql = """UPDATE wikitext SET text='{0}', editnumber={1}, count={2} WHERE title='{3}';""".format(text, result, count, pagename)
        print(sql)
        curs.execute(sql)
        conn.commit()
        return True

def createrecent(title, id, rumber, count):
    sql = """insert into recentchange(Title, rnumber, changer, changetime, count)
            values (%s, %s, %s, now(), %s)"""
    curs.execute(sql, (title, rumber, id, count))
    conn.commit()
    return True

def checkrnumber(title):
    sql = """select * from wikitext where title=%s"""
    curs.execute(sql, title)
    rows = curs.fetchall()
    for row in rows:
        return row[3]