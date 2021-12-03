from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse  
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
	


	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

	@property
	def photo_url(self):
		if self.photo and hasattr(self.photo, 'url'): return self.photo.url 




class Contact(models.Model):
	user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
	user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add = True, db_index = True)	
	

	class Meta:
		ordering = ('-created', )

	def __str__(self):
		return f'{self.user_from} follows {self.user_to}'

	

	
user_model = get_user_model()
user_model.add_to_class('following', 
	models.ManyToManyField('self', through=Contact,
	 related_name='followers', 
	 symmetrical=False))





	