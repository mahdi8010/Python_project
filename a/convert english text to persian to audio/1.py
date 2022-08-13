from gtts import gTTS
import translators

#text =str(input("farsi ? "))
text="هندوانه"
p2=translators.google(text,form_language="fa",to_language="en")



speech = gTTS(p2)


speech.save("sound.mp3")