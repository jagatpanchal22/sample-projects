from rest_framework import serializers
from . import models


class CompanySerializer(serializers.ModelSerializer):
    # Serializer for the Company model, in fields we specify the model attributes we want to
    # deserialize and serialize
    class Meta:
        model = models.Company
        # fields = ['id', 'name', 'location']
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # ingredients = serializers.SerializerMethodField('get_ingredients')
    #
    # def encode_thumbnail(self, recipe):
    #     with open(os.path.join(settings.MEDIA_ROOT, recipe.thumbnail.name), "rb") as image_file:
    #         return base64.b64encode(image_file.read())
    #
    # def get_ingredients(self, recipe):
    #     try:
    #         recipe_ingredients = models.Ingredient.objects.filter(recipe__id=recipe.id)
    #         return IngredientSerializer(recipe_ingredients, many=True).data
    #     except models.Ingredient.DoesNotExist:
    #         return None

    def create(self, validated_data):
        """
        Create function for recipes, a restaurant and a list of ingredients is associated. The restaurantId
        is taken from the corresponding path parameter and the ingredients can be added optionally in the post body.
        """
        # ingredients_data = validated_data.pop("ingredients")
        order = models.Order.objects.create(**validated_data)
        return order

    class Meta:
        model = models.Order
        # fields = ['id', 'summary', 'by_company', 'order_date', 'status']
        fields = '__all__'
