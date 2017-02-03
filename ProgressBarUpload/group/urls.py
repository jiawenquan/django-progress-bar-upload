from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^create-group/$',views.CreateGroup.as_view(),name='create-group'),

]
