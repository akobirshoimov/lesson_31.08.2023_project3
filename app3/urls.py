from django.urls import path
from .views import AllCreateView,DelUpdateDetailView

urlpatterns = [
    path('all/',AllCreateView.as_view()),
    path('detail/<int:detail_id>',DelUpdateDetailView.as_view())
]