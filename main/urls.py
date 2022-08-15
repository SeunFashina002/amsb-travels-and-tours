from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('education/', views.education, name="education"),
    path('business/', views.business, name="business"),
    path('medical/', views.medical, name="medical"),
    path('tourism/', views.tourism, name="tourism"),
    path('agreement/', views.agreement, name="agreement"),
    path('apply/', views.form, name="form"),
]