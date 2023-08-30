from django.urls import path
from .views import all,detail

urlpatterns = [
    path('all/',all),
    path('detail/<int:detail_id>',detail)
]