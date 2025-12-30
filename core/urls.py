from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Project URLs
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    # Hobby URLs
    path('hobbies/', views.hobby_list, name='hobby_list'),
    path('hobbies/create/', views.hobby_create, name='hobby_create'),
    path('hobbies/<int:pk>/', views.hobby_detail, name='hobby_detail'),
    path('hobbies/<int:pk>/update/', views.hobby_update, name='hobby_update'),
    path('hobbies/<int:pk>/delete/', views.hobby_delete, name='hobby_delete'),
    # Profile URLs
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/create/', views.profile_create, name='profile_create'),
    path('profiles/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('profiles/<int:pk>/update/', views.profile_update, name='profile_update'),
    path('profiles/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
]
