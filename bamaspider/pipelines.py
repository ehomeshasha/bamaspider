# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

class BamaPipeline(object):

    msg_tn = "js_weixin_msg"
    content_tn = "js_weixin_content"

    def process_item(self, item, spider):

        timestamp = str(int(time.time()))

        if spider.name == "bamaspider":



            title = item['title']
            digest = item['digest']
            content = item['content']
            fileid = item['fileid']
            content_url = item['content_url']
            source_url = item['source_url']
            cover = item['cover']
            author = item['author']




            # insert_sql = "REPLACE INTO `"+self.msg_tn+"` "\
            #                 "(`title`,`digest`,`content`,`fileid`,`content_url`,`source_url`,`cover`,`author`,`timestamp`) VALUES "\
            #                 "('"+title+"','"+digest+"','"+content+"','"+fileid+"','"+content_url+"','"+source_url+"','"\
            #                 +cover+"','"+author+"','"+timestamp+"')"

            insert_sql = "REPLACE INTO `%s`"\
                            "(`title`,`digest`,`content`,`fileid`,`content_url`,`source_url`,`cover`,`author`,`timestamp`) VALUES "\
                            "('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                            (self.msg_tn, title, digest, content, fileid, content_url, source_url, cover, author, timestamp)
            #print insert_sql

            spider.mysqlClient.query(insert_sql)



        elif spider.name == "weixin_content_spider":

            fileid = item['fileid']
            user_name = item['user_name']
            nick_name = item['nick_name']
            round_head_img = item['round_head_img']
            title = item['title']
            desc = item['desc']
            content = item['content']
            create_time = item['create_time']
            cdn_url = item['cdn_url']
            link = item['link']
            source_url = item['source_url']
            can_share = item['can_share']
            alias = item['alias']
            fakeid = item['fakeid']
            type = item['type']
            author = item['author']
            is_limit_user = item['is_limit_user']
            show_cover_pic = item['show_cover_pic']
            ori_create_time = item['ori_create_time']
            user_uin = item['user_uin']
            total_item_num = item['total_item_num']
            is_async = item['is_async']
            comment_id = item['comment_id']
            img_format = item['img_format']
            svr_time = item['svr_time']
            can_reward = item['can_reward']
            signature = item['signature']



            # insert_sql = "REPLACE INTO `"+self.content_tn+"` "\
            #                 "(`fileid`,`user_name`,`nick_name`,`round_head_img`,`title`,`desc`,`content`"\
            #                 ",`create_time`,`cdn_url`,`link`,`source_url`,`can_share`,`alias`,`fakeid`"\
            #                 ",`type`,`author`,`is_limit_user`,`show_cover_pic`,`ori_create_time`,`user_uin`"\
            #                 ",`total_item_num`,`is_async`,`comment_id`,`img_format`,`svr_time`,`can_reward`"\
            #                 ",`signature`,`timestamp`) VALUES "\
            #                 "('"+fileid+"','"+user_name+"','"+nick_name+"','"+round_head_img+"','"+title+"','"+desc+"','"+content+"','"\
            #                 +create_time+"','"+cdn_url+"','"+link+"','"+source_url+"','"+can_share+"','"+alias+"','"+fakeid+"','"\
            #                 +type+"','"+author+"','"+is_limit_user+"','"+show_cover_pic+"','"+ori_create_time+"','"+user_uin+"','"\
            #                 +total_item_num+"','"+is_async+"','"+comment_id+"','"+img_format+"','"+svr_time+"','"+can_reward+"','"\
            #                 +signature+"','"+timestamp+"')"


            insert_sql = "REPLACE INTO `%s` "\
                            "(`fileid`,`user_name`,`nick_name`,`round_head_img`,`title`,`desc`,`content`,"\
                            "`create_time`,`cdn_url`,`link`,`source_url`,`can_share`,`alias`,`fakeid`,"\
                            "`type`,`author`,`is_limit_user`,`show_cover_pic`,`ori_create_time`,`user_uin`,"\
                            "`total_item_num`,`is_async`,`comment_id`,`img_format`,`svr_time`,`can_reward`,"\
                            "`signature`,`timestamp`) VALUES "\
                            "('%s','%s','%s','%s','%s','%s','%s'," \
                            "'%s','%s','%s','%s','%s','%s','%s'," \
                            "'%s','%s','%s','%s','%s','%s'," \
                            "'%s','%s','%s','%s','%s','%s'," \
                            "'%s','%s')" % \
                            (self.content_tn, fileid, user_name, nick_name, round_head_img, title, desc, content,
                            create_time, cdn_url, link, source_url, can_share, alias, fakeid,
                            type, author, is_limit_user, show_cover_pic, ori_create_time, user_uin,
                            total_item_num, is_async, comment_id, img_format, svr_time, can_reward,
                            signature, timestamp)

            update_sql = "UPDATE `%s` "\
                            "SET `status`=1 WHERE `fileid`='%s'" % \
                            (self.msg_tn, fileid)


            print insert_sql

            spider.mysqlClient.query(insert_sql)
            spider.mysqlClient.query(update_sql)


        return item
