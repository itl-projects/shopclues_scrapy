# -*- coding: utf-8 -*-
import scrapy


class MobilesSpider(scrapy.Spider):
    name = 'mobiles'
    start_urls = ['https://www.shopclues.com/mobiles-smartphones.html?&page=1']
    page = 2

    def parse(self, response):
        data = response.css('div.row')
        for d in data:
            col = d.css('div.column.col3')
            for c in col:
                name = c.css('.prod_name::text').extract_first()
                price = c.css('.p_price::text').extract_first()
                discount = c.css('.prd_discount::text').extract_first()

                yield {

                    'name': name,
                    'price': price,
                    'discount': discount
                }
        next_page ='https://www.shopclues.com/mobiles-smartphones.html?&page='+str(MobilesSpider.page)
        if MobilesSpider.page <= 6:
            MobilesSpider.page +=1
            yield response.follow(next_page, callback=self.parse)


