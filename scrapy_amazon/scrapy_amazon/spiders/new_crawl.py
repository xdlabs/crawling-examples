import scrapy
from bs4 import BeautifulSoup
from scrapy_amazon.items import ScrapyAmazonItem


class NewSpider(scrapy.Spider):
    name = "categories"

    allowed_domains = ["amazon.in"]

    start_urls = ["http://www.amazon.in/gp/site-directory/ref=nav_shopall_btn"]

    def parse(self, response):
        html = response.body
        soup = BeautifulSoup(html, 'html.parser')
        for a in soup.find_all("a", {"class": "nav_a"}):
            url = response.urljoin(a['href'])
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        new_html = response.body
        new_soup = BeautifulSoup(new_html, 'html.parser')
        for a in new_soup.find_all("a", {"class": "title ntTitle noLinkDecoration"}):
            link = response.urljoin(a['href'])
            yield scrapy.Request(link, self.parse_data)

    def parse_data(self, response):
        data = response.body
        soup_data = BeautifulSoup(data, 'html.parser')
        item = ScrapyAmazonItem()

        item["url"] = response.url
        for h1 in soup_data.find_all("h1", {"id": "title"}):
            for name in soup_data.find_all("span", {"id": "productTitle"}):
                print "\n name : ", name.text
                item["name"] = name.text

        for price in soup_data.find_all("span", {"id": "priceblock_ourprice"}):
            if price.text:
                item["price"] = ' '.join(price.text.split())

        for sp in soup_data.find_all("span", {"id": "priceblock_saleprice"}):
            item["price"] = ' '.join(sp.text.split())

        for rate in soup_data.find_all("span", {"class": "a-size-base a-color-price s-price a-text-bold"}):
            if rate.text:
                item["price"] = ' '.join(rate.text.split())

        for reviews in soup_data.find_all("span", {"id": "acrCustomerReviewText"}):
            item["reviews"] = reviews.text

        for div in soup_data.find_all("div", {"id": "avgRating"}):
            span = div.find("span")
            item["stars"] = ' '.join(span.text.split())

        for span in soup_data.find_all("span", {"class": "a-color-base"}):
            for span1 in span.find_all("span", {"class": "a-color-price"}):
                item["price"] = ' '.join(span1.text.split())

        for div in soup_data.find_all("div", {"id": "nav-subnav"}):
            a = div.find("a", {"class": "nav-a nav-b"})
            span = a.find("span", {"class": "nav-a-content"})
            category = span.text
            print "category : ", category
            item["category"] = category
            yield item
