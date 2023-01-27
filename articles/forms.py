from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'content'] #fields to be rendered on form

	def clean(self):
		data = self.cleaned_data

		title = data.get('title')
		# Checks to see if the same title already exists in the database with {field}__icontain = variable
		qs = Article.objects.filter(title__icontains=title)
		if qs:
			self.add_error('title', f'{title} is already used. Please choose another title')

		return data

class ArticleFormOld(forms.Form):
	title = forms.CharField()
	content = forms.CharField()

	# def clean_title(self):
	# 	cleaned_data = self.cleaned_data
	# 	title = cleaned_data('title')
	# 	# Used to add validation to forms
	# 	if title.lower().strip() == 'the movie':
	# 		raise forms.ValidationError('This title is not allowed')
	# 	return title


	def clean(self):
		cleaned_data = self.cleaned_data
		title = cleaned_data('title')
		# Used to add validation to forms
		if title.lower().strip() == 'the movie':
			self.add_error('title', 'This title is not allowed')
		return cleaned_data
