import random
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save,post_save
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

from .utils import slugify_instance_title

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups) 

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

# Create your models here.
class Article(models.Model):
	user = models.ForeignKey(User, blank=True,null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True,null=True, blank=True)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Null and Blank allows field to be empty in the db and django respectively
	# Comment out or delete field to remove column
	publish = models.DateField(auto_now_add=False,null=True, blank=True)

	objects=ArticleManager()

	@property
	def name(self):
		return self.title

	def get_slug_absoluter_url(self):
		return reverse("article-slug-detail", kwargs={"slug": self.slug})

	def get_id_absoluter_url(self):
		return reverse("article-detail", kwargs={"id": self.id})

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