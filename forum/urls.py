from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/', views.ticket, name='ticket'),
    path('<int:ticket_id>/', views.detail, name='detail'),
    path('data/', views.data, name='data'),
    path('view/', views.view, name='view'),

]