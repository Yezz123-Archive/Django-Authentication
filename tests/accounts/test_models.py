import pytest

from django.contrib.auth import get_user_model

pytestmark = pytest.mark.django_db


class TestUser:
    def test_create_user(self, user):
        assert len(user.username) > 0
        assert len(user.email) > 0
        assert user.is_staff is False
        assert user.is_active

    def test___str__(self, user):
        assert str(user) == user.email

    def test_create_superuser(self, admin_user):

        assert len(admin_user.username) > 0
        assert len(admin_user.email) > 0
        assert admin_user.is_staff
        assert admin_user.is_superuser
        assert admin_user.is_active
