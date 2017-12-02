from django.conf.urls import url, include

from moip import views

app_name = 'moip'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='indexview'),
    #url(r'^api/signup/$', SignUpView.as_view(), name='signupview'),
]
