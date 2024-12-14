from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Creat',views.Creat,name='Creat'),
    path('',views.List,name='list'),
    path('edit/<pk>',views.Edit,name='Edit'),
    path('Delete/<pk>',views.delete,name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)