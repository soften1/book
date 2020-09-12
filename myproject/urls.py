from django.conf.urls import url
from book import views

urlpatterns = [
    url(r'^home/$',views.index),
    url(r'^login/$',views.login),
    url(r'^quota/$',views.quota),
    url(r'^myquota/$',views.myquota),
    url(r'^admin/$',views.admin),
    url(r'^user/$',views.user)
]
