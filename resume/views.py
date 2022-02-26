from django.shortcuts import render

# Create your views here.
def aboutme(request):
    #return HttpResponse('about')
    return render (request, 'resume/aboutme.html')
