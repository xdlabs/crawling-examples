import requests
from bs4 import BeautifulSoup
import re

url = "http://www.amazon.in/s/ref=lp_4149751031_st?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A4149418031%2Cn%3A4149751031&qid=1450673890&sort=price-asc-rank"

data = requests.get(url)

html_data = data.content

soup = BeautifulSoup(html_data, "html.parser")

link = soup.a

print "link : ", link

####find name of title

title_name = soup.head.title.string
print "title_name : ", title_name

#######tags
###############searching a string ('a')

for tags in soup.find_all('a'):
    print "type(tags) : ", type(tags)
    print "tags name : ", tags.name
    print "tags attrs : ", tags.attrs

    #### for single valued attribute
    if 'href' in tags.attrs:
        print "href : ", tags.attrs['href']

    if 'id' in tags.attrs:
        print "id : ", tags.attrs['id']

    #### for multi-valued attribute like returning in list
    if 'class' in tags.attrs:
        print "class : ", tags.attrs['class']

    #### NavigableString class for string in tag
    if tags.string is not None:

        ####convert tag string into python unicode string
        str = unicode(tags.string)
        print "tags string : ", str
        print "tags string type : ", type(str)

        #### string cannot be edited so we can replace it
        tags.string.replace_with('New String')
        new_str = unicode(tags.string)
        print "new tags string : ", new_str

    print "\n\n"


#### .contents contains list of all tags
head_contents = soup.head.contents
head_length = len(head_contents)
print "head_length : ", head_length
print "contents in head : ", head_contents

body_contents = soup.body.contents
body_length = len(body_contents)
print "body_length : ", body_length
print "contents in body : ", body_contents

##head content list
print "head contents list"
for r in range(head_length):
    print r, " : ", head_contents[r]

##body content list
print "body contents list"
for r in range(body_length):
    print r, " : ", body_contents[r]

####  .children used to iterate over the tags instead of list
for child in soup.head.children:
    print "\n\n\n"
    print "child : ", child


#### .descendants to get all its direct children and children of its direct children
for descendant in soup.head.descendants:
    print "\n\n"
    print "descendant : ", repr(descendant)
    if descendant.string is not None:
        print "descendant string : ", repr(descendant.string)



##### to get all strings in webpage
for string in soup.strings:
    print "string : ", repr(string)

#### it also return strings but removes all blanks
for string in soup.stripped_strings:
    print "stripped string : ", string

print "\n\n\n"

#### to get parent of any tag
print "soup.div.parent.name : ", soup.div.parent.name


#### to get next sibling of any tag
print "soup.head.script.next_sibling : ", soup.head.script.next_sibling
link = soup.a
print "link : ", link
print "link.next_sibling : ", repr(link.next_sibling)

print "\n\n\n"

#### iterate over siblings
for sibling in link.next_siblings:
    print "sibling : ", repr(sibling)

print "\n\n\n"

#### iterate over elements
#for element in link.next_elements:
#    print "element : ", repr(element)


########### searching using a regular expression

for tags in soup.find_all(re.compile("^a")):
    print "tags name : ", tags.name
    print "tags attributes : ", tags.attrs


####### search all tags starting with word "t"
print "\n\n\n searching tags starting with 't'"
for tags in soup.find_all(re.compile('t')):
    print 'tags in searching: ', tags


###########searching a list
for tags in soup.find_all(["a", "head"]):
    print "tags in list : ", tags


#############using True, returns all tag names available in document
for tags in soup.find_all(True):
    print "tags in True : ", tags.name