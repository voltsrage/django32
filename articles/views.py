from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from .forms import ArticleForm

from .models import Article
# Create your views here.

def article_search_view(request):
	query = request.GET.get('q')
	qs = Article.objects.search(query=query)
	context= {
		"object_list": qs,
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

		# return redirect("article-detail",slug=article_object.slug)
		# return redirect(article_object.get_id_absoluter_url())
	
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

def article_detail_slug_view(request, slug=None):
	# get a single article from database
	article_obj = None

	if slug is not None:
		try:
			article_obj = Article.objects.get(slug=slug)
		except Article.DoesNotExist:
			raise Http404
		except Article.MultipleObjectsReturned:
			article_obj = Article.objects.filter(slug=slug).first()
		except:
			raise Http404

	context = {
		"object": article_obj,
	}

	return render(request,"articles/detail.html",context=context)