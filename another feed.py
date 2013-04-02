from xml.dom import minidom
import urllib.request
import re
import json

response = urllib.request.urlopen("http://www.newsisfree.com/HPE/xml/feeds/85/2085.xml")
xml = response.read()

# get all XML as a string
xml_data = minidom.parseString(xml).getElementsByTagName('channel')

# get all items
parts = xml_data[0].getElementsByTagName('item')

try :
    file=open("try.html","w",encoding='utf-8')
except :
    file=open("try.html","x",encoding='utf-8')
file.write("<!DOCTYPE>\n")
file.write("<html>\n")
file.write("<head>\n")
file.write('    <link rel="stylesheet" href="style.css" type="text/css"/>\n')
file.write('    <meta charset="UTF-8" />\n')
file.write("</head>\n")
file.write("<body>\n")

js=[]
k=0

# loop all items
for part in parts:
    # get title
    title = part.getElementsByTagName('title')[0].firstChild.nodeValue.strip()
    
    # get link
    link = part.getElementsByTagName('link')[0].firstChild.nodeValue.strip()
    stlink = "<a href="+link+">"
    link = 'Link : '+link
    
    # get description
    description = part.getElementsByTagName('description')[0].firstChild.wholeText.strip()
    description = re.sub("<[^>]*>", "", description)
    description = description[:-10]
    
    # get author
    author = part.getElementsByTagName('author')[0].firstChild.nodeValue.strip()
    
    # get lastBuildDate
    lastBuildDate = part.getElementsByTagName('lastBuildDate')[0].firstChild.nodeValue.strip()
    
    # convert to json
    jso=json.dumps({'title': title, 'link': link, 'description': description, 'author': author, 'lastBuildDate': lastBuildDate}, sort_keys=True, indent=4, separators=(',', ': '))
    js.append(jso)
        
    # display info
    j=json.loads(jso)
    file.write("    <div>\n        <p class='title'>\n            ")
    file.write(j['title'])
    file.write("\n        </p>\n")
    file.write("        <p class='lastbd'>\n            ")
    file.write(j['lastBuildDate'])
    file.write("\n        </p>\n")
    file.write("        <h2>\n            ")
    file.write(j["description"])
    file.write("\n        </h2>\n        ")
    file.write(stlink)
    file.write(j['link'])
    file.write("</a>\n        <p class='author'>\n            ")
    file.write(j['author'])
    file.write("\n        </p><br/>\n")
    file.write("    </div>\n")
file.write("</body>\n")
file.write("</html>\n")
file.close()
try :
    file=open("json.txt","w")
except :
    file=open("json.txt","x")
for s in range(1,len(js)):
    file.write(str(js[s]))
    file.write('\n')
file.close()
try :
    file=open("style.css","w")
except :
    file=open("style.css","x")
file.write('body {\n    background-color: black;\n}\n')
file.write('div {\n    display: block;\n    background-color: white;\n    border-radius: 9px;\n    width: 1200px;\n    margin-left: 60px;\n    margin-top: 25px;\n    color: black;\n    font-family: "Trebuchet MS", Helvetica, sans-serif;    }\n\n')
file.write('.title {\n    text-align: center;\n    font-size: 23.5px;\n    font-style: bold;\n    font-family:"Times New Roman", Times, serif;\n    }\n\n')
file.write('a {\n    text-decoration: none;\n    margin-left: 20px;\n    }\n\n')
file.write('a:hover {\n    text-decoration: underline;\n    }\n\n')
file.write('h2 {\n    margin-left: 7px;\n    font-size: 19px;\n    }\n\n')
file.write('.lastbd {\n    text-align: right;\n    margin-right: 4px;\n    font-size: 15px;\n    }\n\n')
file.write('.author {\n    text-align: right;\n    margin-right: 4px;\n    font-size: 17px;\n    }\n')
file.close()
