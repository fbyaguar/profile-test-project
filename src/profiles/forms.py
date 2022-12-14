from django import forms

from profiles.models import Profile


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'biography',
            'contacts',
        ]
