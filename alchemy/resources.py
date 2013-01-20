from tastypie.api import Api
from tastypie.resources import NamespacedModelResource as ModelResource
from alchemy.models import Item, Challenge, Recipe, Player, Solution, Steps


class ItemResource(ModelResource):
	class Meta:
		queryset = Item.objects.all()


class RecipeResource(ModelResource):
	class Meta:
		queryset = Recipe.objects.all()


class ChallengeResource(ModelResource):
	class Meta:
		queryset = Challenge.objects.all()


class PlayerResource(ModelResource):
	class Meta:
		queryset = Player.objects.all()


class SolutionResource(ModelResource):
	class Meta:
		queryset = Solution.objects.all()


class StepsResource(ModelResource):
	class Meta:
		queryset = Steps.objects.all()


api = Api(api_name="v1")
api.register(ItemResource())
api.register(RecipeResource())
api.register(ChallengeResource())
api.register(PlayerResource())
api.register(SolutionResource())
api.register(StepsResource())
