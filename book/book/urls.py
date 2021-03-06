"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from book_info import views
from django.views.static import serve
from book import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:cate_id>/', views.book, name="book"),
    path('book/add/', views.book_add, name="book_add"),
    path('book/delete/<int:book_id>/', views.book_delete, name="book_delete"),
    path('cate/delete/<int:cate_id>/', views.cate_delete, name="cate_delete"),
    path('register/', views.register, name="register"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
