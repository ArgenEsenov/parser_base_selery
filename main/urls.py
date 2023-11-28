from django.urls import path
from .import views



urlpatterns = [
    path('', views.create, name='create'),
    path('read/', views.read, name='read'),
    path('update/<int:id>/', views.edit, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('create_category/', views.CategoryView.as_view()),
    path('create_image/', views.ImageView.as_view()),
    path('create_ads/', views.AdsView.as_view())

]
