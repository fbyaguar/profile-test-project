from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse

from profiles.forms import ProfileUpdateForm
from profiles.models import Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    lookup_field = 'uuid'
    model = Profile
    template_name = 'profiles/profile_detail.html'
    form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        return Profile.objects.get(uuid=self.kwargs.get("uuid"))

    def get_success_url(self):
        return reverse('profiles:profile_detail', kwargs={'uuid': self.object.uuid})


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'
