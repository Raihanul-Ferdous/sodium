from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

from user.models import sign

# Create your views here.

def home(request):
    user_list = sign.objects.all()
    user_dict = {'user':user_list}
    return render(request,'account/prof.html',context=user_dict)
    #return render(request, 'account/prof.html')


#def users(request):
