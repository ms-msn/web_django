from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('vacancy/<int:id>/', views.detail, name='detail'),
    path('vendor/<name>/', views.vend_teh, name='vend_teh'),
    path('listing/', views.listing, name='listing'),
]