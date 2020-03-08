from django.urls import path
from apps.netbankingapp.views import UserViewSet, AccountViewSet, TransactionViewSet
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-user/', UserViewSet.as_view({'put': 'create_user'})),
    path('users/', UserViewSet.as_view({'get': 'list_user'})),
    path('users/<uuid:pk>/', UserViewSet.as_view({'get': 'user_details'})),
    path('users/<uuid:pk>/delete/', UserViewSet.as_view({'get': 'delete_user'})),
    path('users/<uuid:pk>/create-account/', AccountViewSet.as_view({'put': 'create_account'})),
    path('users/<uuid:pk>/accounts/', AccountViewSet.as_view({'get': 'list_accounts'})),
    path('users/<uuid:pk>/accounts/<uuid:account_id>/action/', AccountViewSet.as_view({'put': 'bank_action'})),
    path('users/<uuid:pk>/transactions/', TransactionViewSet.as_view({'get': 'list_transactions'})),

]
