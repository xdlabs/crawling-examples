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
    print "\n\n"
    print "CITY : ", ' '.join(city.split())


######## clinic details


print "\n\t\tDOCTOR DETAILS\n"

for name in soup.find('h1', itemprop="name"):
    print "Name : \t\t\t\t\t", ' '.join(name.string.split())

for qual in soup.find('p', {'class': 'doctor-qualifications'}):
    print "\nQualification : \t\t", ' '.join(qual.string.split())

for div in soup.find_all('div', {'class': 'profile-container'}):
    h2 = div.find('h2')
    spec_exp = ' '.join(h2.text.split())
    new_text = spec_exp.split(',')
    speciality = new_text[0]
    print "\nSpecialization : \t\t", ' '.join(speciality.split())
    experience = new_text[1]
    print "\nExperience : \t\t\t", ' '.join(experience.split())


div = soup.find('div', {'class': 'doc-info-section organizations-block'})
exp = div.find('span', {'class': 'exp-tenure'})
print "\t\t\t\t\t\t", ' '.join(exp.text.split())
exp1 = div.find('span', {'class': 'exp-details'})
print "\t\t\t\t\t\t", ' '.join(exp1.text.split())

print "\nEducation : "

for div in soup.find_all('div', {'class': 'doc-info-section qualifications-block'}):
    for p in div.find_all('p'):
        print "\t\t\t\t\t\t", ' '.join(p.text.split())


div = soup.find('div', {'class': 'doc-info-section memberships-block'})
for p in div.find('p'):
    print "\nMemberships : \t\t\t", ' '.join(p.split())

print "\nRegistrations : "
div = soup.find('div', {'class': 'doc-info-section registrations-block'})
reg = div.find('span', {'class': 'exp-tenure'})
print "\t\t\t\t\t\t", ' '.join(reg.text.split())
reg1 = div.find('span', {'class': 'exp-details'})
print "\t\t\t\t\t\t", ' '.join(reg1.text.split())


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
        print "Clinic Name : \t\t\t", ' '.join(name.text.split())

    for address in clinic.find_all('p', itemprop="address"):
        print "\nAddress : \t\t\t\t", ' '.join(address.text.split())

    print "\nTimings : \t\t\t\t", timing_list[i]
    print "\nDays : \t\t\t\t\t", timing_days[i]
    print "\nFees : \t\t\t\t\t", fees_list[i]
    print "\nLocation : \t\t\t\t", clinic_location[i]

    i = i+1


######## services

print "\n\n\t SERVICES\n"
i = 1
for div in soup.find_all('div', {'class': 'services-block'}):
    for service in div.find_all('div', {'class': 'service-cell'}):
        service_name = ' '.join(service.text.split())
        print i, " : \t", service_name
        i = i+1

