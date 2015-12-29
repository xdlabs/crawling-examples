import scrapy
from bs4 import BeautifulSoup
import re
import urllib2


class SpiderExample(scrapy.Spider):
    name = "new_example"

    start_urls = ["http://www.dmoz.org/"]

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, 'html.parser')

        f = open("crawled_data.txt", "a")

        print "Categories ..."
        f.write("Categories ...")

        for div in soup.find_all("div", {'class': 'one-third'}):
            for span in div.find_all('span'):
                print "\n\n Category Name : ", span.string
                f.write("\n\n Category Name : %s" % span.string)
                a = span.find('a')
                link = a['href']
                url = response.urljoin(link)
                #print "url : ", url
                new_data = urllib2.urlopen(url).read()
                soup = BeautifulSoup(new_data, 'html.parser')
                print "It includes ..."
                f.write("\n\t It includes ...")
                i = 1
                for ul in soup.find_all('ul', {'class': 'directory dir-col'}):
                    for li in ul.find_all('li'):
                        a = li.find('a')
                        print "\t", i, " : ", a.string
                        f.write("\n\t\t  {0} : {1}".format(i, a.string.encode('utf8')))
                        sub_url = response.urljoin(a['href'])
                        sub_pages = urllib2.urlopen(sub_url).read()
                        sub_soup = BeautifulSoup(sub_pages, 'html.parser')
                        title = sub_soup.find("title").text
                        print "\n\t\t Sub Category Name : ", title
                        f.write("\n\t\t\t Sub Category Name : %s" % title)
                        j = 1
                        print "\n\t It further includes .... "
                        f.write("\n\t\t\t\t It further includes .... ")
                        for ul in sub_soup.find_all('ul', {'class': 'directory dir-col'}):
                            for li in ul.find_all('li'):
                                a = li.find('a')
                                print "\t\t", j, " : ", a.string
                                f.write("\n\t\t\t\t {0} : {1}".format(j, a.string.encode('utf8')))
                                j=j+1
                        i=i+1
        f.close()
