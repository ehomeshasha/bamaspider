# -*- coding: utf-8 -*-

# Scrapy settings for bamaspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
#import MySQLdb
BOT_NAME = 'bamaspider'

SPIDER_MODULES = ['bamaspider.spiders']
NEWSPIDER_MODULE = 'bamaspider.spiders'


ITEM_PIPELINES = {
    'bamaspider.pipelines.BamaPipeline': 0,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bamaspider (+http://www.yourdomain.com)'




#mysql connection parameters
MYSQL_HOST="127.0.0.1"
MYSQL_PORT=3306
MYSQL_USER="root"
MYSQL_PASSWD="root"
MYSQL_DBNAME="js_xiudang"
MYSQL_CHARSET="utf8"

#MYSQL_CONN=MySQLdb.connect(host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USER,passwd=MYSQL_PASSWD,db=MYSQL_DBNAME)
