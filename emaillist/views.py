from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
    emaillist = Emaillist.objects.all().order_by('-id')
    data = {'emaillist': emaillist}
    return render(request, 'emaillist/index.html', data)


def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    emalilist = Emaillist()
    emalilist.first_name = request.POST['fn']
    emalilist.last_name = request.POST['ln']
    emalilist.email = request.POST['email']

    emalilist.save()

    return HttpResponseRedirect('/emaillist')


