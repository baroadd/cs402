import requests
from bs4 import BeautifulSoup




def findMethod(url):
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all("button")#Find button tags
    funcName = [] #List of function name
    for x in data:
        if x.get('onclick'):
            funcName.append(x.get('onclick'))
    return funcName
    
def findAllScript(url):
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all("script")
    allScriptList = ''
    for x in data:
        allScriptList = allScriptList + x.get_text()
    return allScriptList
