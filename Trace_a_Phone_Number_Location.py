import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone

phone_number1 = phonenumbers.parse("+59163474542")
phone_number2 = phonenumbers.parse("+971553860509")
phone_number3 = phonenumbers.parse("+919990508070")
phone_number4 = phonenumbers.parse("+79153872211")

print("\nPhone Number Location:\n")
print(phonenumbers.format_number(phone_number4, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(phone_number4, phonenumbers.PhoneNumberFormat.NATIONAL))
print(phonenumbers.format_number(phone_number4, phonenumbers.PhoneNumberFormat.E164))
print(timezone.time_zones_for_number(phone_number4))
print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));
print(geocoder.description_for_number(phone_number4, "en"));


# Answer: Phone Number Location:

#         +971 55 386 0509
#         055 386 0509
#         +971553860509
#         ('Asia/Dubai',)
#         Bolivia
#         United Arab Emirates
#         India
#         Russia
