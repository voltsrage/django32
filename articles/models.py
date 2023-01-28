import random
from django.db import models
from django.db.models.signals import pre_save,post_save
from django.utils import timezone
from django.utils.text import slugify

from .utils import slugify_instance_title
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True,null=True, blank=True)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Null and Blank allows field to be empty in the db and django respectively
	# Comment out or delete field to remove column
	publish = models.DateField(auto_now_add=False,null=True, blank=True)

	#Add additional functionality/ override original save function
	def save(self, *args,**kwargs) :
		# Auto create slug if none is given
		# if self.slug is None:
		# 	self.slug = slugify(self.title)
				# slugify_instance_title(self,save=False)
		super().save(*args,**kwargs)


# things to do before saving resource
def article_pre_save(sender,instance,*args,**kwargs):
	if instance.slug is None:
			slugify_instance_title(instance,save=False)

pre_save.connect(article_pre_save,sender=Article)

# things to do after saving resource
# After needs to add 'instance.save()', since the instance had already been created
def article_post_save(sender,instance,created,*args,**kwargs):
	if created:
			slugify_instance_title(instance,save=True)

post_save.connect(article_post_save,sender=Article)