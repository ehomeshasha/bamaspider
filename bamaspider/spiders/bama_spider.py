# -*- coding: utf-8 -*-
import os
import math
from scrapy.selector import HtmlXPathSelector
from bamaspider.items import BamaspiderItem
from scrapy.spider import Spider
from scrapy.http.request import Request
from scrapy.conf import settings
import json
import MySQLdb
from bamaspider.mysql_client import MysqlClient
from bamaspider.item_process import process_item

class BamaSpider(Spider):

    name = 'bamaspider'
    start_urls = []

    history_url_tn = "js_weixin_history_url"
    add_param = "&f=json&count=9999"

    def parse(self, response):

        #print response.body
        #获取页面内容
        ret = json.loads(response.body)
        if ret['ret'] != 0:
            expired_url = response.url.replace(self.add_param, "")
            print "url "+expired_url+" is expired"
            self.mysqlClient.query("update "+self.history_url_tn+" set status=-1 where url='"+expired_url+"'")
            return

        #获取消息内容
        general_msg_list_obj = json.loads(ret['general_msg_list'])
        #print ret['general_msg_list']
        #获取消息作者
        #msg_author = general_msg_list_obj['author']
        #获取消息list
        msg_list = general_msg_list_obj['list']




        for msg in msg_list:

            app_msg_ext_info = msg['app_msg_ext_info']
            ext_item = BamaspiderItem()

            #ext_item['title'] = app_msg_ext_info['title']
            #ext_item['digest'] = app_msg_ext_info['digest']
            #ext_item['content'] = app_msg_ext_info['content']
            #ext_item['fileid'] = app_msg_ext_info['fileid']
            #ext_item['content_url'] = app_msg_ext_info['content_url']
            #ext_item['source_url'] = app_msg_ext_info['source_url']
            #ext_item['cover'] = app_msg_ext_info['cover']
            #ext_item['author'] = app_msg_ext_info['author']

            ext_item['title'] = process_item(app_msg_ext_info, 'title')
            ext_item['digest'] = process_item(app_msg_ext_info, 'digest')
            ext_item['content'] = process_item(app_msg_ext_info, 'content')
            ext_item['fileid'] = process_item(app_msg_ext_info, 'fileid')
            ext_item['content_url'] = process_item(app_msg_ext_info, 'content_url')
            ext_item['source_url'] = process_item(app_msg_ext_info, 'source_url')
            ext_item['cover'] = process_item(app_msg_ext_info, 'cover')
            ext_item['author'] = process_item(app_msg_ext_info, 'author')

            yield ext_item

            multi_app_msg_item_list = app_msg_ext_info['multi_app_msg_item_list']

            for m in multi_app_msg_item_list:
                item = BamaspiderItem()

                item['title'] = process_item(m, 'title')
                item['digest'] = process_item(m, 'digest')
                item['content'] = process_item(m, 'content')
                item['fileid'] = process_item(m, 'fileid')
                item['content_url'] = process_item(m, 'content_url')
                item['source_url'] = process_item(m, 'source_url')
                item['cover'] = process_item(m, 'cover')
                item['author'] = process_item(m, 'author')

                yield item
            pass






        #print len(msg_list)
        #print msg_author

        #print general_msg_list_obj


        #response.xpath()

        #tag_a = hxs.select('//ul[contains(@class, "category-list")]/li/a')

        #for i, url in enumerate(tag_a.select('@data-path').extract()):
        #    url = self.filter_url + url.replace("%", "%25").replace("+", "%2B")
        #    yield Request(url, callback=self.extract_url, meta={
        #         'catelevel_1': self.df.SimpleFormat(tag_a.select('text()[normalize-space(.)]').extract()[i])})
            #break
    def extract_url(self, response):

        pass
        #hxs = HtmlXPathSelector(response)
        #tag_a = hxs.select('//ul[contains(@class, "category-list")]/li/a')

        #for i, url in enumerate(tag_a.select('@data-path').extract()):
        #    url = self.filter_url + url.replace("%", "%25").replace("+", "%2B")
        #    yield Request(url, callback=self.extract_pagination_url, meta={
        #        'catelevel_1': response.meta['catelevel_1'],
        #        'catelevel_2': self.df.SimpleFormat(tag_a.select('text()[normalize-space(.)]').extract()[i])})
        #    #break


    def closed(self, reason):
        #self.conn.close()
        #self.cursor.close()
        self.mysqlClient.close()



    def __init__(self, name=None, **kwargs):

        self.mysqlClient = MysqlClient(host=settings['MYSQL_HOST'],
                                    port=settings['MYSQL_PORT'],
                                    user=settings['MYSQL_USER'],
                                    passwd=settings['MYSQL_PASSWD'],
                                    db=settings['MYSQL_DBNAME'],
                                    charset=settings['MYSQL_CHARSET'])
        #print "select url from "+self.history_url_tn+" where status>=0"
        self.url_list = self.mysqlClient.fetchAll("select url from "+self.history_url_tn+" where status>=0")
        # self.conn = MySQLdb.connect(host=settings['MYSQL_HOST'],
        #                             port=settings['MYSQL_PORT'],
        #                             user=settings['MYSQL_USER'],
        #                             passwd=settings['MYSQL_PASSWD'],
        #                             db=settings['MYSQL_DBNAME'])

        #self.cursor=self.conn.cursor()
        #self.cursor.execute("select url from "+self.history_url_tn+" where status>=0")
        for row in self.url_list:
            url = row[0] + self.add_param
            self.start_urls.append(url)
            #break

        super(BamaSpider, self).__init__(name, **kwargs)