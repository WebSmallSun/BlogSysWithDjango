from django.conf.urls import url
from Blog import views

urlpatterns = [
    url(r'^$', views.Home, name="Home"),
]
