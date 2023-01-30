from django import forms

from .models import Recipe,RecipeIngredient

class RecipeForm(forms.ModelForm):
	
	# name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter recipe name"}))
	# description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Enter recipe description", "row":3}))
	# directions = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Enter recipe direction", "row":3}))
	class Meta:
		model = Recipe
		fields = ['name', 'description', 'directions'] #fields to be rendered on form

	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		#if you need htmx on field
		new_data = {
			"class": "form-control",
			"placeholder":"Enter ingredient name",
			"hx-post":".",
			"hx-trigger":"keyup changed",
			"hx-post":"#recipe-container",
			"hx-swap":"outerHTML",
		}
		self.fields['name'].widget.attrs.update({"class": "form-control", "placeholder":"Enter recipe name"})
		self.fields['description'].widget.attrs.update({"rows":3,"class": "form-control", "placeholder":"Enter recipe description"})
		self.fields['directions'].widget.attrs.update({"rows":3,"class": "form-control", "placeholder":"Enter recipe direction"})


class RecipeIngredientForm(forms.ModelForm):
	class Meta:
		model = RecipeIngredient
		fields = ['name', 'quantity', 'unit'] #fields to be rendered on form

	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		
		self.fields['name'].widget.attrs.update({"class": "form-control", "placeholder":"Enter ingredient name"})
		self.fields['quantity'].widget.attrs.update({"class": "form-control","type":"number", "placeholder":"Enter quantity"})
		self.fields['unit'].widget.attrs.update({"class": "form-control", "placeholder":"Enter unit"})