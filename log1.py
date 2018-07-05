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
cur = conn.cursor()

# Build Query String
query = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """
conn = psycopg2.connect(dbname='news')
cur = conn.cursor()
cur.execute(query)
res = cur.fetchall()
print('\n more number of errors were encountered on:')
for i in re:
    d = i[0].strftime('%B %d, %Y')
    e = str(round(i[1]*100, 1)) 
    print(d + " with " + e + "percentage")
cur.close()
conn.close()
