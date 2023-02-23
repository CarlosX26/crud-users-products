from django.urls import path
from products.views import ProductView, ProductViewById

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<int:id>/", ProductViewById.as_view()),
]
