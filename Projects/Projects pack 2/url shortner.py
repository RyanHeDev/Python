# url shortner 

import pyshorteners

shortener = pyshorteners.Shortener()
long_link = input("Enter link: ")
short_link = shortener.tinyurl.short(long_link)
print(short_link)

