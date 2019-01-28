#!/usr/bin/env python3

from django.core.management.base import BaseCommand, CommandError

import os
import re
import sqlite3
from urllib.request import *

class Post:
    '''
    Post class, used to store post title & link
    '''
    def __init__(self, p_title, p_link):
        self.title = p_title
        self.post_link = p_link

class Tecmundo:
    '''
    API to fetch from Tecmundo
    '''
    def __init__(self):
        self.link = 'https://www.tecmundo.com.br'

        # call the fetcher and store-it
        self.info = [Post(item[1], item[0]) for item in self.fetch()]

    def fetch(self):
        # Will return a tuple with (link, post_title)
        pattern = re.compile(r'''href="([^"]+)"\sclass="nzn-main-item"\stitle="([^"]+)''')

        try:
            page = urlopen(Request(self.link)).read().decode('UTF-8')
        except Exception as e:
            print(e)
            exit()

        news_obj = re.findall(pattern, page)

        if len(news_obj) == 0:
            raise Exception("Could not find any title on the website!")
        else:
            return news_obj

class TecmundoNews:
    '''
    Different API to fetch from news page on tecmundo
    '''
    def __init__(self):
        self.link = 'https://www.tecmundo.com.br/novidades?page='
        self.page = 1
        self.info = [Post(item[1], item[0]) for item in self.fetch()]

    def fetch(self):
        pattern = re.compile(r'''<h3\sclass="nzn-news-title\suk-margin-remove"[^>]+><a data-bind="[^"]+"\shref="([^"]*)">([^<]+)''')

        news_obj = []

        for i in range(1,6):
            print("Fetching page {}...".format(i))
            try:
                c_page = urlopen(Request(self.link+str(i))).read().decode('UTF-8')
                print("\tPAGE: {}".format(self.link+str(i)))
                log_f = open('log.html', 'w')
                log_f.write(c_page)
            except Exception as e:
                print(e)
                exit()

            found = re.findall(pattern, c_page)
            print(found)
            for new in found:
                print("Appending: {}".new[1])
                #  news_obj.append(new)

        return news_obj

class Command(BaseCommand):
    help = 'Irá alimentar o banco de dados com as noticias atuais'

    def handle(self, *args, **options):
        table_title = 'home_post'
        print("Creating Database")

        # dbect and set the cursor
        db = sqlite3.connect('db.sqlite3')
        cur = db.cursor()

        # create/define database table
        cur.execute("CREATE TABLE IF NOT EXISTS %s(title TEXT, link TEXT)" % table_title) # prod title, link

        print("Starting to fetch from Tecmundo")
        news_titles = Tecmundo().info
        #  news_titles = TecmundoNews().info

        print("Fetched successfully, now inserting into the database")
        print("-"*50)

        # Get the actual posts already in the database (so we don't insert again)
        cur.execute("SELECT title FROM %s" % table_title)
        curr_posts = [x[0] for x in cur.fetchall()]

        for item in news_titles:
            print("'{}' - '{}...'".format(item.title, item.post_link[0:30]))

            # Insert only if not already on there
            if item.title not in curr_posts:
                cur.execute("INSERT INTO %s(title,link) VALUES(?, ?)" % table_title,
                            (item.title, item.post_link))
                db.commit()
        print("-"*50)

        cur.close()
        db.close()
