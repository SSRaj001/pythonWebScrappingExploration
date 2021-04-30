import urllib.request
import urllib.parse

address1 = urllib.request.urlopen("https://docs.python.org/3/library/urllib.request.html")
print(address1.read(100))

# Downloading a Image from a given URL
image = urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/0/02"
                                   "/Sebastian_Vettel_2013_Malaysia_FP1.jpg", "RB9.jpg")

# Downloading a PDF from a given URL
pdf = urllib.request.urlretrieve('https://intranet.cb.amrita.edu/sites/default/files'
                                 '/2020_2021_Academic_calendar_29_MAR_2021.pdf', "Academic_Calendar.pdf")

# # URL Parsers

# URL Parse
parse1 = urllib.parse.urlparse("https://github.com/SSRaj001/pythonWebScrappingExploration")
print(parse1)

# URL Unparse
parsed2URL = urllib.parse.urlunparse(parse1)
print(parsed2URL)

# URL Split
split = urllib.parse.urlsplit(
    "https://www.google.com/search?q=rb9&sxsrf=ALeKk00_T1W-2zu_B8QA_-HPTMOtkAtDeQ%3A1619766105789&source=hp&ei=WauLYLLgLZOE4-EP5u-r4AU&iflsig=AINFCbYAAAAAYIu5aWh6pOvpBlHvpJ2cAYSWF13_KQem&oq=rb9&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyCwguELEDEMcBEKMCMgsILhCxAxDHARCjAjIECAAQQzoHCCMQ6gIQJ1DKEFikF2D2GGgBcAB4AIAB3gGIAacDkgEDMi0ymAEAoAEBqgEHZ3dzLXdperABCg&sclient=gws-wiz&ved=0ahUKEwjy8Oj6sqXwAhUTwjgGHeb3ClwQ4dUDCAY&uact=5")
print(split)

# URL Unsplit
unSplit = urllib.parse.urlunsplit(split)
print(unSplit)

# URL Exceptions

try:
    testURL = urllib.request.urlopen('https://github.com/SSRaj001/search?q=SSR')
    print(testURL.read(100))
except Exception as e:
    print("Exception " + str(e))
