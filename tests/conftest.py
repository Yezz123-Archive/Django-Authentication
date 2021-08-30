import pytest

from .accounts.factories import UserFactory


pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user():
    return UserFactory()
