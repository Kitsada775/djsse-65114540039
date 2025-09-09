from django.contrib import admin
from django.urls import path
from sse_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sse/', views.event_stream_view, name='event_stream'),
]