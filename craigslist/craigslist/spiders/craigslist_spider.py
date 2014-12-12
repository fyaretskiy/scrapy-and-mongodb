import scrapy

from craigslist.items import craigslist_item 

class CraigsList(scrapy.Spider):
    name = "craigslist"
    allowed_domains = ["http://www.craigslist.com"]
    start_urls = ["http://newyork.craigslist.org/bka/"]

    def parse(self, response):
        print "parse works"
        for sel in response.xpath('/html/body/article/div/div/div'
                                  '[@class=\'content\']/p'):
            print "here is the item", sel
            item = craigslist_item()
            item['title'] = sel.xpath('span/span[@class="pl"]/a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item

         

         #'//@href'