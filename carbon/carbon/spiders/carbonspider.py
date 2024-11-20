import scrapy

class CarbonSpider(scrapy.Spider):
    name = 'carbon'
    start_urls = ['https://carbon38.com/en-in/collections/tops?filter.p.m.custom.available_or_waitlist=1']

    def parse(self,response):
        for products in response.css('div.ProductItem'):
            try:
                yield {
                    'name':products.css('h2.ProductItem__Title.Heading a::text').get() ,
                    'price':products.css('span.ProductItem__Price.Price::text').get() ,
                    'designer':products.css('h3.ProductItem__Designer::text').get(),
                    

                }
            except:
                yield {
                    'name':products.css('h2.ProductItem__Title.Heading a::text').get() ,
                    'price':'SALE' ,
                    'designer':products.css('h3.ProductItem__Designer::text').get(),
                    
                    

                }

        next_page =response.css('a.next').attrib['href']
        
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)   
    


