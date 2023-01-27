from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ArticleForm

from .models import Article
# Create your views here.

def article_search_view(request):
	query_dict = request.GET # this is a dictionary
	# Check query is an integers

	try:
		query = int(query = query_dict.get("q"))
	except:
		query = None

	article_obj = None
	if query is not None:
		article_obj = Article.objects.get(id=query)

	context= {
		"object": article_obj,
	}
	return render(request,"articles/search.html",context=context)

@login_required
def article_create_view(request,):
	# create a single article and add to database

	#Allows form to read as both GET (if None) or POST
	form = ArticleForm(request.POST or None)
	context = {	
		"form":form
	}

	if form.is_valid():
		# With forms.ModelForm
		article_object = form.save()
		# Create a blank form after submitting
		context['form'] = ArticleForm()
		# With forms.Form
		# title = form.cleaned_data.get('title')
		# content = form.cleaned_data.get('content')

		# article_object = Article.objects.create(title=title,content=content)

		context['object'] = article_object
		context['created'] = True
	
	return render(request,"articles/create.html",context=context)

def article_detail_view(request, id=None):
	# get a single article from database
	article_obj = None

	if id is not None:
		article_obj = Article.objects.get(id=id)

	context = {
		"object": article_obj,
	}

	return render(request,"articles/detail.html",context=context)