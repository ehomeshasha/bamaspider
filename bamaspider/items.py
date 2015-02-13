# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BamaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    digest = scrapy.Field()
    content = scrapy.Field()
    fileid = scrapy.Field()
    content_url = scrapy.Field()
    source_url = scrapy.Field()
    cover = scrapy.Field()
    author = scrapy.Field()

    pass

class WeixinContentItem(scrapy.Item):

    fileid = scrapy.Field()
    user_name = scrapy.Field()
    nick_name = scrapy.Field()
    round_head_img = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    content = scrapy.Field()
    create_time = scrapy.Field()
    cdn_url = scrapy.Field()
    link = scrapy.Field()
    source_url = scrapy.Field()
    can_share = scrapy.Field()
    alias = scrapy.Field()
    fakeid = scrapy.Field()
    type = scrapy.Field()
    author = scrapy.Field()
    is_limit_user = scrapy.Field()
    show_cover_pic = scrapy.Field()
    ori_create_time = scrapy.Field()
    user_uin = scrapy.Field()
    total_item_num = scrapy.Field()
    is_async = scrapy.Field()
    comment_id = scrapy.Field()
    img_format = scrapy.Field()
    svr_time = scrapy.Field()
    can_reward = scrapy.Field()
    signature = scrapy.Field()


