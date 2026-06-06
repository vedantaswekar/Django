from django.contrib import admin
from django.urls import path
from studentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.student)
]
