import scrapy

class craigslist_item(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    
    pass