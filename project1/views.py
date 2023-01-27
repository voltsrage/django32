"""
To render html web pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article




def home_view(request, *args, **kwargs):
	"""
	Take in request (Django sends request)
	Return HTML as a response (We chose response)
	"""

	# from database

	# one item by id
	article_obj = Article.objects.get(id=1)

	# all items
	article_queryset = Article.objects.all()

	context = {
		"object_list":article_queryset,
		"title":article_obj.title,
		"id":article_obj.id,
		"content":article_obj.content
	}

	#Django Templates
	HTML_STRING = render_to_string("home-view.html",context=context)

	return HttpResponse(HTML_STRING)