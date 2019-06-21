from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')


def hello2(request, id=0):
    return HttpResponse(f'id:{id}')


def hello3(request):
    jsonresult = {
        'result': 'success',
        'data': ['hello', 1, 2, True, ('a', 'b', 'c')]
    }

    return JsonResponse(jsonresult)


def insert(request):
    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save()

    return HttpResponse('ok')


def max(request):
    value = Counter.objects.aggregate(gnomax=Max('groupno'))
    return HttpResponse(f'max:{value["gnomax"]}')


def update(request):
    Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno')+1)
    return HttpResponse('ok')
