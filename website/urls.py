
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/' , views.logout_user, name='logout'),
    path('register/' , views.register_user, name='register'),
    path('record/<int:pk>' , views.customer_record, name='record'),
    path('delete_record/<int:pk>' , views.delete_record, name='delete'),
    path('add_record' , views.add_record, name='add_record'),
    path('update_record/<int:pk>' , views.update_record, name='update_record'),
    path('record_info/<int:pk>', views.show_record_info , name = 'show_record_info'),
    path('give_items/<int:pk>' , views.give_items , name='give_items'),
    path('process_give', views.process_give , name="process_give")
]