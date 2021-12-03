from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	search_fields = ['user__username', 'user__email']
	list_display = ['user', 'date_of_birth', 'photo']

	
			