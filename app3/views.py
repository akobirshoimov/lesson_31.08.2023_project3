from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import StudentsModel,TeachersModel
from rest_framework import generics
from .serializer import StudentsSerializer,TeachersSerializer
from rest_framework.permissions import IsAuthenticated  


# Create your views here.
class AllCreateView(generics.ListAPIView):
    queryset= StudentsModel.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        print(self.request.user)
        return StudentsModel.objects.all()

class DelUpdateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= StudentsModel.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return TeachersModel.objects.all()





# def detail(request,detail_id):
#     each = Teachers.objects.get(id=detail_id)
#     each = get_object_or_404(Teachers,id= detail_id)
#     info = f'teacher name:{each.name},date_of_birth {Teachers.date_of_birth}'
#     return JsonResponse(info)

# def all(request):
#     all = Students.objects.all()
#     result = []
#     for i in all:
#         result.append({
#             'name': i.name,
#             'date_of_birth': i.date_of_birth
#         })
#     return JsonResponse(result,safe=False)





