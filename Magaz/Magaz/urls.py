from django.contrib import admin
from django.urls import path
from books.views import CreateBook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CreateBook,name='create-book')
]
