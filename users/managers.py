from django.contrib.auth.models import BaseUserManager


class UserManagerCustom(BaseUserManager):
    def create_user(self, first_name, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email), first_name=first_name, **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, email, password, **extra_fields):
        user = self.create_user(first_name, email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
