from django.urls import path
from . import views

app_name = 'ninjas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailsView.as_view(), name='details'),
    path('<int:dev_id>/level/', views.level, name='level'),

]