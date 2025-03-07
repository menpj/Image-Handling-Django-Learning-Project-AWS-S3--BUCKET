from django.urls import path
from . import views


urlpatterns = [
    path('',views.upload_form, name='upload_form'),
    path("list/",views.list_dogs, name='list_dogs'),
    path("delete/<int:pk>/",views.delete_image, name='delete_image')
]