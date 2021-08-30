import pytest

from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed

from pages.views import HomePageView


class TestHomepageView:
    @pytest.fixture()
    def response(self, client):
        yield client.get("/")

    def test_homepage_status_code(self, response):
        assert response.status_code == 200

    def test_homepage_url_name(self, client):
        response = client.get(reverse("pages:index"))
        assert response.status_code == 200

    def test_homepage_template(self, response):
        assertTemplateUsed(response, "pages/index.html")

    def test_homepage_contains_correct_html(self, response):
        assert b"<h1>Homepage</h1>" in response.content

    def test_homepage_does_not_contain_incorrect_html(self, response):
        assert b"<h1>This is incorrect</h1>" not in response.content

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        assert view.func.__name__ == HomePageView.as_view().__name__
