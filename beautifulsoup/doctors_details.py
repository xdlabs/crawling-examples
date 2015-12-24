from bs4 import BeautifulSoup
import re


filename = "page.html"
with open(filename, "rb") as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')


######### city name

for div in soup.find_all('div', {'class': 'location-container'}):
    span = div.find('span')
    city = span.string
    print "city : ", re.sub('\s+', '', city)


######## clinic details

for div in soup.find_all('div', {'class': 'profile-container'}):
    #print "div : ", div
    name = div.find('h1', itemprop="name")
    print "name : ", re.sub('\s+', '', name.string)

    qual = div.find('p', {'class': 'doctor-qualifications'})
    print "qualification : ", re.sub('\s+', '', qual.string)

    h2 = div.find('h2')
    spec_exp = re.sub('\s+', '', h2.text)
    new_text = spec_exp.split(',')
    speciality = new_text[0]
    print "specialization : ", speciality
    experience = new_text[1]
    print "experience : ", experience

    clinic_locality = div.find('div', {'class': 'clinic-locality'})
    print "clinic locality : ", re.sub('\s+', '', clinic_locality.text)

    clinic_detail = div.find('div', {'class': 'clinic-address'})
    name = clinic_detail.find('h2')
    print "clinic name : ", re.sub('\s+', '', name.text)

    address = clinic_detail.find('p')
    print "clinic address : ", re.sub('\s+', '', address.text)

    timing = div.find('div', {'class': 'clinic-timings'})

    timing_day = timing.find('p', {'class': 'clinic-timings-day'})
    print "days : ", re.sub('\s+', '', timing_day.text)

    timing_session = timing.find('p', {'class': 'clinic-timings-session'})
    print "timings : ", re.sub('\s+', '', timing_session.text)

