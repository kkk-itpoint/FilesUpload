from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def Index(request):
    return render(request, 'profiles/index.html')

def Profiles(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            #n1 = form.cleanded_data.get('fname')
            form.save()
            obj = form.instance
            return render(request, 'profiles/profile.html', {'form':form, 'obj':obj})
        else:
            return render(request, 'profiles/profile.html', {'form':form})
    else:
        form = ProfileForm()
        return render(request, 'profiles/profile.html', {'form':form})
    
def GetProfiles(request):
    if request.method == 'GET':
        rows = Info.objects.all()
        return render(request, 'profiles/getprofiles.html', {'rows':rows})
        
def DeleteProfile(request, id):
    b = Info.objects.get(id = id)
    if request.method == 'POST':
        b.delete()
        return GetProfiles(request)
    else:
        return render(request, 'profiles/delete_confirm.html')
    
def SearchProfile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['profile_id']
            return redirect('/readbook/' + str(id))
    else:
        form = ProfileForm
    return render(request, 'profiles/searchprofile.html', {'form':form})

def ReadProfile(request, id):
    try:
        row = Info.objects.get(id = id)
    except Exception:
        row = None
    return render(request, 'profiles/readprofile.html', {'row':row})