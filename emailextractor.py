# Use the HTTP GET Method 
# to get the source code of a web page and extract all emails

import requests,re,pyperclip
url = pyperclip.paste()

getwebsite = requests.get(url)
print(f"Succseful GET {getwebsite.url} ==> ",getwebsite.status_code)
website_content = getwebsite.text

compile = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",re.DOTALL|re.I)
findemail = compile.findall(website_content)

for i in set(findemail) :
    print("Found email =+> ",i)
