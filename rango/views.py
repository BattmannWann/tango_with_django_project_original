from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    
    #boldmessage matches to the {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    
    #note that the first parameter below is the TEMPLATE WE WISH TO USE
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    
    context_dict = {'boldmessage': "This tutorial has been put together by Rhys Stewart."}
    
    return render(request, "rango/about.html", context = context_dict)