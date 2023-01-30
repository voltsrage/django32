from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError

from .models import RecipeIngredient, Recipe

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')

    def test_user_pw(self):
        checked = self.user_a.check_password("abc123")
        self.assertTrue(checked)

    

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')

				#recipes
        self.recipe_a = Recipe.objects.create(
            name='Grilled Chicken',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='Grilled Chicken Tacos',
            user = self.user_a
        )

				#recipe ingredients
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='1/2',
            unit='pound'
        ) 
				
        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='asdadasd',
            unit='pound'
        )

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a 
				# _set will give a queryset of the recipes that a given user has
				# i.e, library.book_set.all() give me all the books in the library
        qs = user.recipe_set.all() 
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_forward_count(self):
        user = self.user_a 
				# get all the recipes form user_as
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(), 2)

    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a 
        qs = recipe.recipeingredient_set.all() 
        self.assertEqual(qs.count(), 2)

    def test_recipe_ingredientcount(self):
        recipe = self.recipe_a 
				# get all the ingredients for recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation(self):
        user = self.user_a
				# get all the ingredients for user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 2)
    
    def test_user_two_level_relation_reverse(self):
        user = self.user_a
				# get all the recipe ingredient ids 
				# by getting all the recipes for a user_a and make of list of all of recipeingredient__ids
        recipeingredient_ids = list(user.recipe_set.all().values_list('recipeingredient__id', flat=True))
        qs = RecipeIngredient.objects.filter(id__in=recipeingredient_ids)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation_via_recipes(self):
        user = self.user_a
        ids = user.recipe_set.all().values_list("id", flat=True)
        qs = RecipeIngredient.objects.filter(recipe__id__in=ids)
        self.assertEqual(qs.count(), 2)

    def test_unit_measure_validation(self):
      invalid_unit = 'nada'
			# How to test validation errors 
      with self.assertRaises(ValidationError):
        ingredient = RecipeIngredient(
					name='New',
					quantity=10,
					recipe=self.recipe_a,
					unit=invalid_unit
				)
      ingredient.full_clean()

    def test_quantity_as_float(self):
      self.assertIsNone(self.recipe_ingredient_a.quanity_as_float)
      self.assertIsNotNone(self.recipe_ingredient_b.quanity_as_float)