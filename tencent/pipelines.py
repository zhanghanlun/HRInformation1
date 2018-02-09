# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


class TencentPipeline(object):
    #初始化函数
    def __init__(self):
        #打开json文件
        self.f = open("tencent.json", "w")
        # self.db = pymysql.connect(host="localhost", user="root",
        #                           password="zhanghanlun",
        #                           database="zhanghanlun",
        #                           charset='utf8',
        #                           cursorclass=pymysql.cursors.DictCursor)



    def process_item(self, item, spider):
        # cursor=self.db.cursor()
        # d=dict(item)
        # PName=d['positionName'][0]
        # PNumber=d['peopleNumber'][0]
        # PLocation=d['workLocation'][0]
        # sql = 'insert into hr values("'+PName+'",'+PNumber+',"'+PLocation+'");'
        # print(sql)
        # try:
        #     cursor.execute(sql)
        #     self.db.commit()
        #     print("chenggong")
        # except Exception as e:
        #     self.db.rollback()
        #     print("失败")
        #     print(e)

        #存储数据到json文件中
        content = json.dumps(dict(item)) + ", \n"
        self.f.write(content)

        return item

    def close_spider(self, spider):
        # self.db.close()
        #关闭open函数
        self.f.close()
