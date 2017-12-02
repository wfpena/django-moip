from django.conf.urls import url

from moip import views

app_name = 'moip'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='indexview'),
]
