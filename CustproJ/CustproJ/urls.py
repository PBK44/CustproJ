
from django.contrib import admin
from django.urls import path,re_path
from TestApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^home$',views.homeview),
    re_path(r'^custinfo$',views.custview)
]
