
from django.conf.urls import url,include
from django.urls import path
from . import views
urlpatterns = [
    url(r'^$',views.app2_home)
]
