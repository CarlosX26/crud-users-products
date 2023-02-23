from django.contrib.auth.models import AbstractUser
from users.managers import UserManagerCustom
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=128, unique=True)
    first_name = models.CharField(max_length=64)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManagerCustom()

    class Meta:
        db_table = "users"

    def __repr__(self) -> str:
        return f"<User ({self.id}) - {self.email}>"
