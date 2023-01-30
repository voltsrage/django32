"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from .views import home_view
from articles.views import (
	article_search_view,
	article_create_view,
	article_detail_view,
	article_detail_slug_view,
)

from accounts.views import (
	login_view,
	logout_view,
	register_view,
)

from search.views import search_view

urlpatterns = [
	path('',home_view),
	path('pantry/recipes/',include('recipes.urls')),
	# create part for article resources search

	# """Accounts"""
	path('login/',login_view),
	path('logout/',logout_view),
	path('register/',register_view),

	#"""Articles"""
	path('articles/',article_search_view),
		# create part for article resources creation
	path('articles/create/',article_create_view,name='article-create'),
	# create part for retrieving article resources with integer id
	path('articles/<int:id>/',article_detail_view,name='article-detail'),

	path('articles/<slug:slug>/',article_detail_slug_view,name='article-slug-detail'),

	#"""Search"""
	path('search/',search_view, name='search'),

	path('admin/', admin.site.urls),
]
