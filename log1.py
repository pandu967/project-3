#!usr/bin/env python3
import psycopg2
'''article = """select title,count(title) as views
from articles join log on log.path like concat('%',articles.slug,'%')
where log.status like '%200%'
group by articles.title order by views desc limit 3;
"""
conn = psycopg2.connect(dbname='news')
cur = conn.cursor()
cur.execute(article)
print("     TOP THREE ARTICLES")
print("Title                                       Views")
results=cur.fetchall()
for i in range(len(results)):
    title=results[i][0]
    views=results[i][1]
    print("%s--%d" % (title,views))
cur.close()
conn.close()


author = """select authors.name, count(*) as n from articles join
           authors on articles.author=authors.id
           join log on log.path like concat('%',articles.slug,'%')
           where log.status like '%200%' and
           authors.id=articles.author
           group by authors.name
           order by n desc limit 3"""
conn = psycopg2.connect(dbname='news')
cur = conn.cursor()
cur.execute(author)
print("       POPULAR AUTHORS")
print("Author                       Views")
c = cur.fetchall()
for a, n in c:
    print(a, n)
cur.close()
conn.close()
'''
conn = psycopg2.connect(dbname='news')
cur = conn.cursor()
total_request = """select count(*) as count,
        date(TIME) as date
        from log group by date order by count desc"""
error_request = """select count(*) as count,
        date(TIME) as date
        from log
        where log.status!='%200%'
        group by date
        order by count desc"""
err_perc = """select  total_request.date,
        round((100.0*error_request.count)/total_request.count,2) as err_prc
        from error_request,
        total_request where error_request.date=total_request.date"""
error = """select to_char(date, 'Mon DD YYYY')
        as date, err_prc
        from err_prc where err_prc>1.0"""
cur.execute(total_request)
cur.execute(error_request)
cur.execute(err_perc)
c = cur.execute(error)
res = c.fetchall()
for i in range(len(res)):
    d = res[i][0]
    e = res[i][1]
    print("more number of errors were "
          "encountered on "+d+ " with " +e+ " percentage")
cur.close()
conn.close()
