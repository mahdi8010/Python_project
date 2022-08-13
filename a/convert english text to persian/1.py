import translators

text =str(input("farsi ? "))

p2=translators.google(text,form_language="fa",to_language="en")
print(p2)