from django.contrib import admin
from django.urls import path
from fichas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ocra/', views.detalle_ocra, name='detalle_ocra'),
    path('sadida/', views.detalle, name='detalle'),
]
