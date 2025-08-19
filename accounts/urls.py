from django.urls import path

from accounts.views import user_list_or_create, user_update_or_delete

urlpatterns = [
    path('' , user_list_or_create , name='user_list_or_create'),
    path('update/<int:pk>/' , user_update_or_delete , name='user_list_or_create'),
    path('delete/<int:pk>/' , user_update_or_delete , name='user_list_or_create'),
    path('create/' , user_list_or_create , name='user_list_or_create'),
]