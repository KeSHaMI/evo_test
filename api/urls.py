from django.urls import path
from .views import *
urlpatterns = [
    path('get_all/', get_all),
    path('get/<str:pk>', get),
    path('create/', create),

]





