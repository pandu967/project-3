#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    db = psycopg2.connect('dbname=' + DBNAME)
    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    db.close()
    return rows


class log:

    def get_top_articles(self):
        """Returns top 3 most read articles"""

        # Build Query String
        query = """
            SELECT articles.title, COUNT(*) AS num
            FROM articles
            JOIN log
            ON log.path LIKE concat('/article/%', articles.slug)
            GROUP BY articles.title
            ORDER BY num DESC
            LIMIT 3;
        """

        # Run Query
        results = run_query(query)

        # Print Results
        print('\n          TOP THREE ARTICLES BASED ON VIEWS')
        count = 1
        for i in results:
            number = str(count) + '. "'
            title = i[0]
            views = '" with ' + str(i[1]) + " views"
            print(number + title + views)
            count += 1


def get_top_article_authors(self):
        """returns top 3 most popular authors"""

        # Build Query String
        query = """
            SELECT authors.name, COUNT(*) AS num
            FROM authors
            JOIN articles
            ON authors.id = articles.author
            JOIN log
            ON log.path like concat('/article/%', articles.slug)
            GROUP BY authors.name
            ORDER BY num DESC
            LIMIT 3;
        """

        # Run Query
        results = run_query(query)

        # Print Results
        print('\n          TOP THREE AUHOTS BASED ON VIEWS:')
        print('')
        count = 1
        for i in results:
            print(str(count) + '. ' + i[0] + ' with ' + str(i[1]) + " views")
            count += 1


def get_days_with_errors(self):
        """returns days with more than 1% errors"""

        # Build Query String
        query = """
            SELECT total.day,
              ROUND(((errors.error_requests*1.0) / total.r"
              "equests), 3) AS percent
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
            WHERE (ROUND(((errors.error_requests*1.0) / total.reque"
            "sts), 3) > 0.01)
            ORDER BY percent DESC;
        """

        # Run Query
        results = run_query(query)

        # Print Results
        print('\n          DAYS WITH MAORE THAN 1% ERROR:')
        for i in results:
            date = i[0].strftime('%B %d, %Y')
            errors = str(round(i[1]*100, 1)) + "%" + " errors"
            print(date + " -- " + errors)
a = log()
a.get_top_articles()
a.get_top_article_authors()
a.get_days_with_errors()
