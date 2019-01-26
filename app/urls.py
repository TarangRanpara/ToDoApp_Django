from django.urls import path,include
from . import views

urlpatterns = [
    
    path('create/',views.create_view),
    path('update/<int:entry_id>/',views.update_view),
    path('delete/<int:entry_id>/',views.delete_view),
    path('show/',views.show_view),
    path('',views.show_view)
]