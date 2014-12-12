import scrapy

from extra_credit.items import ExtraCreditItem 
from pymongo import MongoClient

client = MongoClient()
craigslist = client.craigslist
barter = craigslist.barter

class CraigsList(scrapy.Spider):
    name = "extracredit"
    allowed_domains = ["http://www.craigslist.com"]
    start_urls = ["http://newyork.craigslist.org/bar"]



    def parse(self, response):
        print "parse works"
        for sel in response.xpath('/html/body/article/div/div/div[@class=\'content\']/p'):
            print "here is the item", sel
            item = ExtraCreditItem()
            item['title'] = sel.xpath('span/span[@class="pl"]/a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            title = item['title']
            link = item['link']
            entry = {"title": title,
                    "link": link}
            barter_id = barter.insert(entry)
            yield item

