# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName=scrapy.Field()

    positionType=scrapy.Field()

    positionLink=scrapy.Field()

    peopleNumber=scrapy.Field()

    workLocation=scrapy.Field()

    publishTime=scrapy.Field()

    positionInformation=scrapy.Field()

class item_Detail(scrapy.Item):


    pName=scrapy.Field()

    pNumber=scrapy.Field()

    pRes=scrapy.Field()

    pRequire=scrapy.Field()


