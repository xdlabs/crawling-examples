import scrapy
from scrapy_example.items import ScrapyExampleItem
from bs4 import BeautifulSoup


class NewSpider(scrapy.Spider):
    name = "example"

    start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"]

    def parse(self, response):
        data = response.body

        item = ScrapyExampleItem()

        soup = BeautifulSoup(data, 'html.parser')
        print soup.prettify()

        title = soup.find('title').text
        print "title : ", title

        ul = soup.find("ul", {'class': 'directory-url'})
        for li in ul.find_all("li"):
            a = li.find('a', {'class': 'listinglink'})
            item['name'] = a.text
            item['link'] = a['href']
            yield item
            print "In this.."
            print "Book Name : ", item['name']
            print "and its link is : ", item['link']
            print "\n\n"
