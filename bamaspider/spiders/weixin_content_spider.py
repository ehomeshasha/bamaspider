# -*- coding: utf-8 -*-
import traceback
import os
import math
from scrapy.selector import HtmlXPathSelector
from bamaspider.items import BamaspiderItem, WeixinContentItem
from scrapy.spider import Spider
from scrapy.http.request import Request
from scrapy.conf import settings
import json
import MySQLdb
from bamaspider.mysql_client import MysqlClient
from bamaspider.item_process import process_item

class WeixinContentSpider(Spider):

    name = 'weixin_content_spider'
    #start_urls = []

    msg_tn = "js_weixin_msg"
    add_param = "f=json&"




    def start_requests(self):

        self.mysqlClient = MysqlClient(host=settings['MYSQL_HOST'],
                                        port=settings['MYSQL_PORT'],
                                        user=settings['MYSQL_USER'],
                                        passwd=settings['MYSQL_PASSWD'],
                                        db=settings['MYSQL_DBNAME'],
                                        charset=settings['MYSQL_CHARSET'])

        query = "select `fileid`,`content_url` from `"+self.msg_tn+"` where `status`=0"
        urllist = self.mysqlClient.fetchAll(query)
        #print len(urllist)
        for url in urllist:
            meta = {}
            fileid = url[0]
            meta['fileid'] = fileid
            content_url = url[1].replace("?__", "?"+self.add_param+"__")

            yield Request(content_url, meta=meta)
            #break

    def parse(self, response):


        ret = json.loads(response.body)
        try:
            base_resp = ret['base_resp']
            if base_resp['ret'] == 0:
                item = WeixinContentItem()
                item['fileid'] = response.meta['fileid']
                item['user_name'] = process_item(ret, 'user_name')
                item['nick_name'] = process_item(ret, 'nick_name')
                item['round_head_img'] = process_item(ret, 'round_head_img')
                item['title'] = process_item(ret, 'title')
                item['desc'] = process_item(ret, 'desc')
                item['content'] = process_item(ret, 'content')
                item['create_time'] = process_item(ret, 'create_time')
                item['cdn_url'] = process_item(ret, 'cdn_url')
                item['link'] = process_item(ret, 'link')
                item['source_url'] = process_item(ret, 'source_url')
                item['can_share'] = process_item(ret, 'can_share')
                item['alias'] = process_item(ret, 'alias')
                item['fakeid'] = process_item(ret, 'fakeid')
                item['type'] = process_item(ret, 'type')
                item['author'] = process_item(ret, 'author')
                item['is_limit_user'] = process_item(ret, 'is_limit_user')
                item['show_cover_pic'] = process_item(ret, 'show_cover_pic')
                item['ori_create_time'] = process_item(ret, 'ori_create_time')
                item['user_uin'] = process_item(ret, 'user_uin')
                item['total_item_num'] = process_item(ret, 'total_item_num')
                item['is_async'] = process_item(ret, 'is_async')
                item['comment_id'] = process_item(ret, 'comment_id')
                item['img_format'] = process_item(ret, 'img_format')
                item['svr_time'] = process_item(ret, 'svr_time')
                item['can_reward'] = process_item(ret, 'can_reward')
                item['signature'] = process_item(ret, 'signature')

                yield item
                pass
        except:
            print traceback.format_exc()



