from django.urls import path
from apps.netbankingapp.views import UserViewSet
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-user/', UserViewSet.as_view({'put': 'create_user'})),
    path('users/', UserViewSet.as_view({'get': 'list_user'})),

]
