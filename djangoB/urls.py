from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.indexgender),
    path('genders/create', views.creategender),
    path('store_gender', views.storegender)
]
