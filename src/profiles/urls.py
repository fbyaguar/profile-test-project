from django.urls import path

from profiles.views import ProfileUpdateView, ProfileListView

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile_list'),
    path('profile/<uuid:uuid>/', ProfileUpdateView.as_view(), name='profile_detail'),
]
