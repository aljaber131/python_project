from django.shortcuts import render

from .model import Profile
# Create your views here.

def homepage(request):
    Profile= Profile.objects.all()
    context = {
        'profile': profile
    }
    
    return render(request,'index.html',context)


