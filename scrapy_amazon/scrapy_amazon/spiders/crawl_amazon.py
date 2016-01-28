import scrapy
from bs4 import BeautifulSoup
from scrapy_amazon.items import ScrapyAmazonItem


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.in"]
    start_urls = ["http://www.amazon.in"]

    def parse(self, response):
        html = response.body
        soup = BeautifulSoup(html, 'html.parser')
        #for a in soup.find_all('a', {"class": "a-link-normal  a-inline-block"}):
        #    new_url = response.urljoin(a['href'])
        #    yield scrapy.Request(new_url, callback=self.parse_content)

        i = 1
        for div in soup.find_all("div", {"class": "desktop-row gw-widget-instrument"}):
            for div1 in div.find_all("div", {"class": "a-section a-spacing-none shogun-widget uber-widget aui-desktop fresh-shoveler"}):
                for div2 in div1.find_all("div", {"class": "a-section feed-carousel"}):
                    for div3 in div2.find_all("div", {"class": "a-section feed-carousel-viewport"}):
                        for ul in div3.find_all("ul", {"class": "a-nostyle a-horizontal feed-carousel-shelf"}):
                            for li in ul.find_all("li", {"class": "feed-carousel-card"}):
                                for span in li.find_all("span", {"class": "a-list-item"}):
                                    for a in span.find_all("a", {"class": "a-link-normal  a-inline-block"}):
                                        url = response.urljoin(a['href'])
                                        print i, " : ", url
                                        i = i+1

    '''
    def parse_content(self, response):
        new_html = response.body
        new_soup = BeautifulSoup(new_html, 'html.parser')
        item = ScrapyAmazonItem()
        for div in new_soup.find_all("div", {"id": "centerCol"}):
            for div1 in div.find_all("div", {"id": "title_feature_div"}):
                for div2 in div1.find_all("div", {"id": "titleSection"}):
                    for h1 in div2.find_all("h1", {"id": "title"}):
                        span = h1.find("span", {"id": "productTitle"})
                        name = span.text
                        item["name"] = name

            for div3 in div.find_all("div", {"id": "price_feature_div"}):
                for div4 in div3.find_all("div", {"id": "price"}):
                    for span in div4.find_all("span", {"id": "priceblock_saleprice"}):
                        price = ' '.join(span.text.split())
                        item["price"] = price

            for div5 in div.find_all("div", {"id": "averageCustomerReviews_feature_div"}):
                for div6 in div5.find_all("div", {"id": "averageCustomerReviews"}):
                    for span in div6.find_all("span", {"id": "acrPopover"}):
                        for span1 in span.find_all("span", {"class": "a-declarative"}):
                            for a in span1.find_all("a", {"class": "a-popover-trigger a-declarative"}):
                                for i in a.find_all("i", {"class": "a-icon a-icon-star a-star-4-5"}):
                                    span = i.find("span", {"class": "a-icon-alt"})
                                    stars = span.text
                                    item["stars"] = stars
                    for a in div6.find_all("a", {"id": "acrCustomerReviewLink"}):
                        span2 = a.find("span", {"id": "acrCustomerReviewText"})
                        reviews = span2.text
                        item["reviews"] = reviews
                        yield item

        for new_div in new_soup.find_all("div", {"class": "a-row a-carousel-controls a-carousel-row a-carousel-has-buttons"}):
            for new_div1 in new_div.find_all("div", {"class": "a-carousel-row-inner"}):
                for new_div2 in new_div1.find_all("div", {"class": "a-carousel-col a-carousel-center"}):
                    for new_div3 in new_div2.find_all("div", {"class": "a-carousel-viewport"}):
                        for ol in new_div3.find_all("ol", {"class": "a-carousel"}):
                            for li in ol.find_all("li", {"class": "a-carousel-card a-float-left"}):
                                for div in li.find_all("div", {"class": "a-section a-spacing-none p13nimp p13n-asin"}):
                                    for a in div.find_all("a", {"class": "a-link-normal"}):
                                        url = response.urljoin(a['href'])
                                        yield scrapy.Request(url, callback=self.parse_content)
    '''