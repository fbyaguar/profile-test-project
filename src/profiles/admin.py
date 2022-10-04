from django.contrib import admin

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'modified', 'created')
    search_fields = ['first_name', 'last_name']
    list_display = ('first_name', 'last_name', 'contacts')


admin.site.register(Profile, ProfileAdmin)
