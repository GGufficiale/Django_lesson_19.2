from django.urls import path
from catalog.views import index
from catalog.apps import MainConfig

app_name = MainConfig.name
urlpatterns = [
    path('', index)
]
