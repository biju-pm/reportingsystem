from django.urls import path
from .views import ProfileUpdateView, ProfileView


urlpatterns = [
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='update_user_profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='user_profile'),
]