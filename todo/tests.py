from django.test import TestCase, Client
from django.urls import reverse
from .views import UserListView, UserCreateView
from .models import User
from django.test import TestCase
from todo.form import UserCreateForm, UserUpdateForm, TaskCreateForm, TaskUpdateForm


class UserListViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("users-list")

    def tearDown(self):
        pass

    def test_should_render_text_empty(self):
        # Arrange
        expected_result = "<td>empty</td>"
        expected_status_code = 200

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertContains(
            result,
            expected_result,
            1,
            expected_status_code
        )
        self.assertTemplateUsed(result, "user_list.html")
        self.assertTrue(list(result.context["object_list"]) == [])


class UserCreateViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("user-create")

    def tearDown(self):
        pass

    def test_create_user_submit_btn(self):
        # Arrange
        expected_result = '<input type="submit" value="Submit">'

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))


class UserUpdateViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("user-update", args=[1])

    def tearDown(self):
        pass

    def test_update_user_submit_btn(self):
        # Arrange
        User.objects.create(
            id=0,
            is_active=False,
            email="xXxKillerxXx@swag.ru",
            password="FF15"
        )

        expected_result = '<input type="submit" value="Submit">'

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))


class UserDetailViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("users-list")

    def tearDown(self):
        pass

    def test_detail_user_submit_btn(self):
        # Arrange
        User.objects.create(
            id=0,
            is_active=False,
            email="uznevimcomampsat@stocked.cz",
            password="rr"
        )

        expected_result = '<input type="submit" value="Submit">'

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))


class UserDeleteViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("users-list")

    def tearDown(self):
        pass

    def test_delete_user_submit_btn(self):
        # Arrange
        User.objects.create(
            id=0,
            is_active=False,
            email="uznevimcomampsat@stocked.cz",
            password="rr"
        )

        expected_result = '<input type="submit" value="Submit">'

        # Act
        result = self.client.get(self.url)

        # Assert
        self.assertInHTML(expected_result, str(result.content))