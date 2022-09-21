from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self, email, first_name, last_name, role, department, password=None
    ):
        if not email:
            raise ValueError("Email is required!!")
        else:

            email = self.normalize_email(email)

            user = self.model(
                email=email,
                first_name=first_name,
                last_name=last_name,
                role=role,
                department=department,
            )

            user.set_password(password)

            user.save(using=self._db)

            return user

    def create_superuser(
        self, email, first_name, last_name, role, department, password
    ):

        user = self.create_user(
            email, first_name, last_name, role, department, password
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
