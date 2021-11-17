from django.shortcuts import render

# Create your views here.
def index(request): #Get and post are the two type of requests
    return render(request, 'MainApp/index.html')
    
