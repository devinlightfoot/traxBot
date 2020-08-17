from django.urls import path
from . import views

app_name = 'traxBotWeb'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('trax/', views.trax, name = 'trax'),
    path('profile/', views.profile, name = 'profile'),
    path('products/', views.products, name = 'products')
]