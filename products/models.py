from django.db import models


class Product(models.Model):

    img_url = models.URLField()
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    is_active = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )

    class Meta:
        db_table = "products"

    def __repr__(self) -> str:
        return f"<Product ({self.id}) - {self.name}>"
