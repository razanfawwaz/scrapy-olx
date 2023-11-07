import scrapy

class OlxSpider(scrapy.Spider):
    name = "olx"
    allowed_domains = ["www.olx.co.id"]

    def start_requests(self):
        base_url = "https://www.olx.co.id/mobil-bekas_c198?page={}"
        for page_number in range(51):  # Loop from page 0 to 50
            url = base_url.format(page_number)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        price = response.css('._1zgtX::text').extract()
        year = response.css('._21gnE::text').extract()
        brand = response.css('._2Gr10::text').extract()

        for item in zip(price, year, brand):
            year_km = item[1].split(' - ')
            extracted_year = year_km[0] if len(year_km) > 0 else 'N/A'  # Extracted year
            extracted_km_range = year_km[1] if len(year_km) > 1 else 'N/A'  # Extracted kilometer range

            scraped_info = {
                'price': item[0],
                'year': extracted_year,
                'kilometers': extracted_km_range,
                'brand': item[2]
            }

            yield scraped_info
