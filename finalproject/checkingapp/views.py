from django.shortcuts import render
from django.http import HttpResponse
from . import findscript

url = 'http://localhost/testHtml.html'
functionName = ['loadDoc()','loadDocVar()']
scriptAll = findscript.findAllScript(url)
listArr = []
context = {
            'var1':functionName[0] ,
            'var2':scriptAll   
        }

def index(request):
        global context
        global listArr
        query = request.GET.get('url')
        if query is not None:
                msg = "{}".format(query)
                listArr.append(msg)
                newContext = {
                        'var1':functionName[1] ,
                        'var2':scriptAll   
                }
                print(listArr)
                context = newContext 
        
                
        return render(request,'index.html',context)   
        
        
        

