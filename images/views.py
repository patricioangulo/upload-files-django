from django.shortcuts import render

# Create your views here.
def addImage(request):
    return render(request, 'images/add.html')