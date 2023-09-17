from django.contrib import admin
from .models import StudentsModel,TeachersModel
# Register your models here.

admin.site.register(StudentsModel)
admin.site.register(TeachersModel)

