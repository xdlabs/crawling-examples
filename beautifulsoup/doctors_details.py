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
    print "CITY : ", re.sub('\s+', '', city)


######## clinic details


print "\n\t\tDOCTOR DETAILS\n"

for name in soup.find('h1', itemprop="name"):
    print "name : ", re.sub('\s+', '', name.string)

for qual in soup.find('p', {'class': 'doctor-qualifications'}):
    print "qualification : ", re.sub('\s+', '', qual.string)

for div in soup.find_all('div', {'class': 'profile-container'}):
    h2 = div.find('h2')
    spec_exp = re.sub('\s+', '', h2.text)
    new_text = spec_exp.split(',')
    speciality = new_text[0]
    print "specialization : ", speciality
    experience = new_text[1]
    print "experience : ", experience


div = soup.find('div', {'class': 'doc-info-section organizations-block'})
exp = div.find('span', {'class': 'exp-tenure'})
print "\t", re.sub('\s+', '', exp.text)
exp1 = div.find('span', {'class': 'exp-details'})
print "\t", re.sub('\s+', '', exp1.text)

print "Education : "

for div in soup.find_all('div', {'class': 'doc-info-section qualifications-block'}):
    for p in div.find_all('p'):
        print '\t', re.sub('\s+', '', p.text)


div = soup.find('div', {'class': 'doc-info-section memberships-block'})
for p in div.find('p'):
    print "Memberships : ", re.sub('\s+', '', p)

print "Registrations : "
div = soup.find('div', {'class': 'doc-info-section registrations-block'})
reg = div.find('span', {'class': 'exp-tenure'})
print "\t", re.sub('\s+', '', reg.text)
reg1 = div.find('span', {'class': 'exp-details'})
print "\t", re.sub('\s+', '', reg1.text)


timing_days = []
timing_list = []
fees_list = []
clinic_location = []

for clinic_locality in soup.find_all('div', {'class': 'clinic-locality'}):
    location = re.sub('\s+', '', clinic_locality.text)
    clinic_location.append(location)

for days in soup.find_all('p', {'class': 'clinic-timings-day'}):
    days = re.sub('\s+', '', days.text)
    timing_days.append(days)

for timing in soup.find_all('p', {'class': 'clinic-timings-session'}):
    time = re.sub('\s+', '', timing.text)
    timing_list.append(time)

for fees in soup.find_all('div', {'class': 'clinic-fees'}):
    span = fees.find('span').text
    fees = re.sub('\s+', '', span)
    fees_list.append(fees)

i = 0

print "\n\n\t\tCLINIC DETAILS"

for clinic in soup.find_all('div', 'clinic-address'):
    print "\n"
    for name in clinic.find_all('h2'):
        print "clinic name : ", re.sub('\s+', '', name.text)

    for address in clinic.find_all('p', itemprop="address"):
        print "address : ", re.sub('\s+', '', address.text)

    print "timings : ", timing_list[i]
    print "days : ", timing_days[i]
    print "fees : ", fees_list[i]
    print "location : ", clinic_location[i]

    i = i+1


######## services

print "\n\n\t SERVICES\n"
i = 1
for div in soup.find_all('div', {'class': 'services-block'}):
    for service in div.find_all('div', {'class': 'service-cell'}):
        service_name = re.sub('\s+', '', service.text)
        print i, " : ", service_name
        i = i+1

