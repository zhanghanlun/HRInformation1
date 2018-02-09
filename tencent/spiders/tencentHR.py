# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem


class TencenthrSpider(scrapy.Spider):
    #项目名称 scrapy crawl 命令下运行该项目
    name = 'tencentHR'
    #项目的爬取页面的域名的范围
    allowed_domains = ['tencent.com']
    base_url="https://hr.tencent.com/position.php?keywords=&lid=0&start="
    offset=0
    #start_urls是每次抓取页面的url链接的集合
    start_urls=[base_url+str(offset)]

    def parse(self, response):
        #职位信息位于下面的这个类
        node_list=response.xpath("//tr[@class='even']|//tr[@class='odd']")

        for node in node_list:
            #定义item对象
            item=TencentItem()
            #获取职位名字信息存到item中
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()
            #获取职位链接信息存储到item中
            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]

            url_second=node.xpath("./td[1]/a/@href").extract()[0]

            #存储到职位类型到item对象中
            if len(node.xpath("./td[2]/text()").extract()):
                item['positionType'] = node.xpath("./td[2]/text()").extract()
            else:
                item['positionType'] = ""

            item['peopleNumber'] = node.xpath("./td[3]/text()").extract()

            item['workLocation']=node.xpath("./td[4]/text()").extract()

            item['publishTime']=node.xpath("./td[5]/text()").extract()




            yield scrapy.Request("https://hr.tencent.com/"+url_second,callback=self.parse_second)

            yield item



        #循环抓取页面
        if len(response.xpath("//a[@id='next' and @class='nocative']"))==0:
            #获取下一个页面的URL地址
            url=response.xpath("//a[@id='next']/@href").extract()[0]
            print(url)
            yield scrapy.Request("https://hr.tencent.com/"+url,callback=self.parse)

        #if self.offset<3200:
        #    self.offset+=10
        #    url=self.base_url+str(self.offset)
         #   yield scrapy.Request(url,callback=self.parse)
    def parse_second(self,response):


        pass



