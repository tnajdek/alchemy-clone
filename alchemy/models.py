from django.db import models


class Item(models.Model):
	"""Represents a single, mixable item"""
	name = models.CharField(max_length=50)
	icon = models.CharField(max_length=50)
	color = models.CharField(max_length=6)		# as RGB hex format e.g. FF0000


class Recipe(models.Model):
	""" Represents a recipe for a single mixture which can have multiple ingredients
		as well as more than one product """
	ingredients = models.ManyToManyField(Item, related_name='ingredients')
	products = models.ManyToManyField(Item, related_name='products')


class Player(models.Model):
	""" Represents a player only by name and it's not a user for simplicity """
	name = models.CharField(max_length=50)


class Challenge(models.Model):
	""" Represents a challenge to build a product starting with ingredients provided """
	name = models.CharField(max_length=50)
	initial_ingredients = models.ManyToManyField(Item, related_name='initial_ingredients')
	product = models.ForeignKey(Item)
	score = models.IntegerField()
	solver = models.ForeignKey(Player)


class Solution(models.Model):
	""" solution to a challenge """
	challenge = models.ForeignKey(Challenge)
	recipes = models.ManyToManyField(Recipe, through='Steps', related_name='recipes')


class Steps(models.Model):
	""" helper class for a m2m relation between Solution and Recipe"""
	recipe = models.ForeignKey(Recipe)
	solution = models.ForeignKey(Solution)
	order = models.IntegerField()
