from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="home"),

    path('signup/', views.signup, name="sign_up"),
    path('login/', views.Login.as_view() , name='login'),

    path('education/', views.education, name="education"),
    path('business/', views.business, name="business"),
    path('medical/', views.medical, name="medical"),
    path('tourism/', views.tourism, name="tourism"),
    path('agreement/', views.agreement, name="agreement"),
    path('apply/', views.form, name="apply"),
    path('success/', views.success_modal, name="success"),
    

    path('logout/', LogoutView.as_view() , name='logout'),

    

]