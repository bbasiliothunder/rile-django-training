from django.urls import path
from members import views

urlpatterns = [
    path('', views.show_members, name='show-members'),
    path('add_new_members/', views.add_new_members, name='add-new-members'),
    path('add_new_members/add_member/', views.add_new_members_process, name='add-new-member-process'),
    path('delete/<int:id>', views.delete_member, name='delete-member'),
    path('update/<int:id>', views.update_member, name='update-member'),
    path('update/update_records_member/<int:id>', views.update_members_process, name='update-member-process')
]