from django.shortcuts import render
from django.http import HttpResponse
from . import findscript

url = 'http://localhost/testHtml.html'
functionName = ['loadDoc()','loadDocVar()']
#scriptAll = findscript.findAllScript(url)
scriptAll = """function loadDoc() {
  console.log('loadDoc()'); //print
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET","demo_get2.asp?fname=Henry&lname=Ford", true);
  xhttp.send();
}

function loadDocVar() {
  console.log('loadDocVar()'); //print
  var hostname = 'https://jsonplaceholder.typicode.com/';
  var path = 'posts/1';
  
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      let json = JSON.parse(xhttp.responseText);
      document.getElementById("title").innerHTML = json.title;
      document.getElementById("content").innerHTML = json.body;
    }
  };
  xhttp.open("GET", hostname + path);
  xhttp.send();
}"""

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
        
        
        

