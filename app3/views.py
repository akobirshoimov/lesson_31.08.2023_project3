from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Students,Teachers

# Create your views here.

def detail(request,detail_id):
    each = Teachers.objects.get(id=detail_id)
    each = get_object_or_404(Teachers,id= detail_id)
    info = f'teacher name:{each.name},date_of_birth {Teachers.date_of_birth}'
    return JsonResponse(info)

def all(request):
    all = Students.objects.all()
    result = []
    for i in all:
        result.append({
            'name': i.name,
            'date_of_birth': i.date_of_birth
        })
    return JsonResponse(result,safe=False)





