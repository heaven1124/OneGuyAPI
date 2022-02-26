from django.urls import path
from .views import UserApi
app_name = 'user'
urlpatterns = [
    path('all/', UserApi.as_view(), name='all'),
]