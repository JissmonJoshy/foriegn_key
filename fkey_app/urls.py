from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_course', views.add_course, name='add_course'),
    path('add_student', views.add_student, name='add_student'),
    path('show_student_details', views.show_student_details, name='show_student_details'),
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),
]
