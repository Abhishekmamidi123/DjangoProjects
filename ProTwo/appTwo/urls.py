from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^users', views.users, name="users"),
    url(r'^help', views.help, name="help"),
]
