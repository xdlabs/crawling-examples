from bs4 import BeautifulSoup
from bs4 import CData

html_doc = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="title"><b>The Dormouse's story</b></p>
            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="www.example.com/elsie" class="sister" id="link1">Elsie</a>,
            <a href="www.example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="www.example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>
            <p class="story">...</p>
        </body>
    </html>"""

soup = BeautifulSoup(html_doc, 'html.parser')

#print soup.prettify()

print "soup.title : ", soup.title

print "soup.title.name : ", soup.title.name

print "soup.title.string : ", soup.title.string

print "soup.title.parent : ", soup.title.parent

print "soup.title.parent.name : ", soup.title.parent.name

print "soup.p : ", soup.p

print "soup.p['class'] : ", soup.p['class']

print "soup.a : ", soup.a

print "soup.find_all('a') : ", soup.find_all('a')

print "soup.find(id='link3') : ", soup.find(id='link3')

print "soup.get_text() : ", soup.get_text()

tag = soup.p
print "tag : ", tag
print "type(tag) : ", type(tag)
print "tag.name : ", tag.name
tag.name = "pr"
print "tag : ", tag
print "tag['class'] : ", tag['class']
print "tag.attrs : ", tag.attrs
tag = soup.a
print "tag : ", tag
print "type(tag) : ", type(tag)
print "tag.name : ", tag.name
print "tag['class'] : ", tag['class']
print "tag.attrs : ", tag.attrs

for tags in soup.find_all('a'):
    print "tags : ", tags
    print "type(tags) : ", type(tags)
    print(tags['href'])

css_tag = BeautifulSoup("<p class='body strikeout' id='my id'></p>")
print "css_tag.p['class] : ", css_tag.p['class']
print "css_tag.p['id'] : ", css_tag.p['id']

new_tag = BeautifulSoup("<p class='body strikeout' id='my id1'>Dummy Value</p>", 'xml')
print "new_tag.p['class'] : ", new_tag.p['class']
print "new_tag.p['id'] : ", new_tag.p['id']
print "new_tag.string : ", new_tag.string
unicode_string = unicode(new_tag.string)
print "unicode_String : ", unicode_string


tag = soup.a
print "tag : ", tag
print "tag.string : ", tag.string
tag.string.replace_with('name')
print "soup.a : ", soup.a

markup = "<b><!-- This is a comment --></b>"
mark_up = BeautifulSoup(markup)
comment = mark_up.string
print "comment : ", comment
print "type of comment : ", type(comment)
print mark_up.prettify()

cdata = CData("A CData Block")
comment.replace_with(cdata)
print "mark_up.prettify() : ", mark_up.prettify()

head_tag = soup.head
print "head_tag : ", head_tag
head_content = head_tag.contents
print "head_content : ", head_content

body_tag = soup.body
print "body_tag : ", body_tag
body_content = body_tag.contents[3]
print "body_content : ", body_content

print "soup.content : ", soup.contents

print "soup.p.contents : ", soup.p.contents

for child in body_content.descendants:
    print "child : ", child

for string in soup.strings:
    print "string : ", string
    print "repr(string)", repr(string)

link = soup.a

print "link.parents : ", link.parents

for parent in link.parents:
    if parent is None:
        print parent
    else:
        print parent.name

for sibling in link.next_siblings:
    print "sibling : ", repr(sibling)


sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>")

a = sibling_soup.a

for child in a.descendants:
    print child

print sibling_soup.b.next_sibling
print sibling_soup.c.previous_sibling

print "link.next_element : ", link.next_element


for tags in soup.find_all(True):
    print "tags.name : ", tags.name


def has_class_but_no_id(tag):
    print tag.has_attr('class')
    return tag.has_attr('class') and not tag.has_attr('id')