#!usr/bin/env python3
import psycopg2
articles = """select articles.titles,
           count(*) as n from log,articles
           where log.status="%200%"
           group by articles.title
           order by n desc limit 3"""
conn = psycopg2.connect(dbname='news')
cur = conn.cursor()
cur.execute(articles)
print("     TOP THREE ARTICLES")
print("Title                                       Views")
c = cur.fetchall()
for title, n in c:
    print(title, n)
cur.close()
conn.close()


authors = """select authors.name, count(*)as n from articles,
           authors, log where log.status="%200%" and
           authors.id=articles.author
           group by authors.name
           order by n desc"""
conn = psycopg2.connect(dbname='news')
cur = cunn.cursor()
cur.execute(authors)
print("       POPULAR AUTHORS")
print("Author                       Views")
c = cur.fetchall()
for a, n in c:
    print(a, n)
cur.close()
conn.close()

conn = psycopg2.connect(dbname='news')
cur = cunn.cursor()
t_req = """select count(*) as c,
        date(TIME) as date
        from log group by date order by c desc"""
e_req = """select count(*) as c,
        date(TIME) as date
        from log
        where log.status="%200%"
        group by date
        order by c desc"""
e_perc = """select  t_req.date,
        round((100.0*e_req.count)/t_req.count,2)
        as e_per from e_req,
        t_req where e_req=t_req"""
error = """select to_char(date, 'Mon DD YYYY')
        as date, e_per
        from e_perc where e_per>1.0"""
try:
    cur.execute(t_req)
    cur.execute(e_req)
    cur.execute(e_perc)
except Exception as e:
    print(e)
c = cur.execute(error)
res = c.fetchall()
for i in range(len(res)):
    d = res[i][0]
    e = res[i][1]
    print("more number of errors were "
          "encountered on "d " with " e " percentage")
cur.close()
conn.close()
