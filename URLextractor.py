# Use the HTTP GET Method 
# to get the source code of a web page and extract all URL's

import requests,re,pyperclip,webbrowser,sys
url = pyperclip.paste()
getwebsite = requests.get(url)
print(f"Succseful GET {getwebsite.url} ==> ",getwebsite.status_code)
website_content = getwebsite.text
compile = re.compile(r"http[s]?://(?:[a-zA-Z]|[$-_@.&+]|(?:[0-9a-fA-F][0-9a-fA-F]))+")
findurl = compile.findall(website_content)
set_findurl = set(findurl)
ask = input('do you want to show all URL\'s :')
if ask == "y" :
    for i in set_findurl :
        print(i)
if ask == "n" :
    sys.exit()
ask2 = input("do you want to open all links :")
if ask2 == "y" :
    for i in set_findurl :
        webbrowser.open(i)
if ask2 == "n" :
    sys.exit()
