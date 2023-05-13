import phonenumbers as pn
from phonenumbers import carrier, geocoder, timezone

num = input('Enter a Number with country code: ')
phone = pn.parse(num)
tz = timezone.time_zones_for_number(phone)
cr = carrier.name_for_number(phone, 'en')
registration = geocoder.description_for_number(phone, 'en')

print(phone)
print(tz)
print(cr)
print(registration)
