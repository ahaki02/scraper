import scrapy

class car_finder(scrapy.Spider):

    name = "dubai_car"

    start_urls = [
        "https://www.dubicars.com/dubai/used",
    ]

    def parse(self, response):

        for item in response.css("div.detail"):
            yield {
                "name" : item.css("div.mt-8::text").get(),
                "price" : item.css("strong::text").get(),
            }

        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)