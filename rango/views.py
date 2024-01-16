from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    
    #boldmessage matches to the {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    
    #note that the first parameter below is the TEMPLATE WE WISH TO USE
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    
    response = """ Rango says here is the about page
    
                    <a href = '/rango/'>Index</a>
                    
               """
    
    return HttpResponse(response)