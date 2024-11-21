from django.shortcuts import render

# from django.http import HttpResponse 
# def test(request):
#     return HttpResponse("test page")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
