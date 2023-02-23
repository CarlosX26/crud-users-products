from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "img_url", "name", "description", "price", "stock", "user_id"]
        read_only_fields = ["user_id"]
        extra_kwargs = {"stock": {"min_value": 1}, "price": {"min_value": 0}}

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
