from bs4 import BeautifulSoup, NavigableString
import urllib2

url = "http://www.amazon.in/s/ref=lp_4149751031_st?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A4149418031%2Cn%3A4149751031&qid=1450673890&sort=price-asc-rank"

#html_data = requests.get(url).content

html_data = urllib2.urlopen(url)

soup = BeautifulSoup(html_data, 'html.parser')


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


for tags in soup.find_all(has_class_but_no_id):
    print "\n\n"
    print "tags : ", tags


def get_links(tag):
    return tag.has_attr('href')


#for tag in soup.find_all(get_links):
#    print "tag : ", tag

for tag in soup(get_links, limit=10):
    print "\n\n"
    print "tag : ", tag


def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString) and isinstance(tag.previous_element, NavigableString))


for div in soup('div', {'class': 'a-row a-spacing-small'}):
    print "\n\n"
    print "div : ", div
    print "div.text : ", div.text
    for a in div("a"):
        print "a : ", a
        print "a.href : ", a.href
