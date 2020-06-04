from django.shortcuts import render
from testApp.models import *
# Create your views here.
def index(request):
    return render(request,'testApp/index.html')

def hyd_jobs(request):
    job_list=hydjobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testApp/hydjobs.html',context=my_dict)


def punejobs(request):
    return render(request,'testApp/punejobs.html')

def chennaijobs(request):
    return render(request,'testApp/chennaijobs.html')

def blorejobs(request):
    return render(request,'testApp/blorejobs.html')
