from django.contrib import admin
from django.urls import path
from content import views as content_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', content_views.post_cr_views),
    path('post/<int:post_id>/', content_views.post_cr_views),
    path('like/', content_views.like_views),
    path('like/<int:pk>/', content_views.like_views),
    path('', content_views.post_cr_views)
]