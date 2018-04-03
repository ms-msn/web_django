from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.listing, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('vendor/<name>/', views.vend_teh, name='vend_teh'),
]