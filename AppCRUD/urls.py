from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('',views.addEmployee,name='addEmployee'),
    path('add_employee_details',views.add_employee_details,name='add_employee_details'),
    path('show_employees',views.show_employees,name='show_employees'),

    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('edit_employee_details/<int:pk>',views.edit_employee_details,name="edit_employee_details"),
    path('delete_employee/<int:pk>',views.delete_employee,name='delete_employee')



    
]