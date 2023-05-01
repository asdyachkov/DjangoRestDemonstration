from rest_framework import status
from rest_framework.test import APITestCase

from library.models import User, Book, Autor


class AccountCreatingTests(APITestCase):
    def test_create_account(self):
        data = {
            "first_name": "Stepan",
            "last_name": "Dyachkov",
            "email": "stepanderdichok@gmail.com",
            "password": "Test1Pass1",
            "username": "Test1",
        }
        response = self.client.post("/api/auth/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "Test1")


class AccountLoginTests(APITestCase):
    def setUp(self):
        data = {
            "username": "Test1",
            "password": "Test1Pass1",
        }
        self.client.post("/api/auth/users/", data)

    def test_login_user(self):
        data = {
            "username": "Test1",
            "password": "Test1Pass1",
        }
        response = self.client.post("/auth/token/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user_wrong_data(self):
        data = {
            "username": "WrongTest1",
            "password": "WrongTest1Pass1",
        }
        response = self.client.post("/auth/token/login/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unlogin_user_getting_info(self):
        response = self.client.get("/api/auth/users/me/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unlogin_user_getting_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unlogin_user_getting_one_book(self):
        response = self.client.get("/api/books/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unlogin_user_adding_book(self):
        data = {
            "name": "Сказка о царе Салтане",
            "description": "«Сказка о царе Салтане» − книга, написанная великим мастером русского слова. Книга рассказывает о женитьбе царя Салтана и дальнейшем появлении на свет его сына по имени князь Гвидон. Из-за козней родных теток Гвидон оказывается на необитаемом острове. Там он встречает могущественную волшебницу, известную как царевна Лебедь.",
            "publish_date": "2023-04-30",
        }
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unlogin_user_update_book(self):
        data = {
            "name": "Edit. Сказка о царе Салтане",
            "description": "Edit. «Сказка о царе Салтане» − книга, написанная великим мастером русского слова. Книга рассказывает о женитьбе царя Салтана и дальнейшем появлении на свет его сына по имени князь Гвидон. Из-за козней родных теток Гвидон оказывается на необитаемом острове. Там он встречает могущественную волшебницу, известную как царевна Лебедь.",
            "publish_date": "2023-05-30",
        }
        response = self.client.put("/api/books/1/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unlogin_user_delete_book(self):
        response = self.client.delete("/api/books/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ApiTests(APITestCase):
    def setUp(self):
        data = {
            "username": "Test1",
            "password": "Test1Pass1",
        }
        self.client.post("/api/auth/users/", data)
        response = self.client.post("/auth/token/login/", data)
        token = response.data["auth_token"]
        self.auth = f"Token {token}"
        Autor.objects.create(
            name="Stepan",
            surname="Dyachkov",
            birth_date="2004-02-14",
        ),
        Book.objects.create(
            name="Сказка о царе Салтане",
            autor_id=1,
            description="«Сказка о царе Салтане» − книга, написанная великим мастером русского слова. Книга рассказывает о женитьбе царя Салтана и дальнейшем появлении на свет его сына по имени князь Гвидон. Из-за козней родных теток Гвидон оказывается на необитаемом острове. Там он встречает могущественную волшебницу, известную как царевна Лебедь.",
            publish_date="2023-04-30",
        )

    def test_get_all_books(self):
        response = self.client.get("/api/books/", HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_one_book(self):
        response = self.client.get("/api/books/1/", HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Сказка о царе Салтане")

    def test_add_new_book(self):
        data = {
            "name": "New Сказка о царе Салтане",
            "autor_id": 1,
            "description": "New «Сказка о царе Салтане» − книга, написанная великим мастером русского слова. Книга рассказывает о женитьбе царя Салтана и дальнейшем появлении на свет его сына по имени князь Гвидон. Из-за козней родных теток Гвидон оказывается на необитаемом острове. Там он встречает могущественную волшебницу, известную как царевна Лебедь.",
            "publish_date": "2023-04-30",
        }
        response = self.client.post("/api/books/", data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["added_book"]["name"], "New Сказка о царе Салтане"
        )
        self.assertEqual(len(Book.objects.all()), 2)

    def test_edit_book(self):
        data = {
            "name": "Edited Сказка о царе Салтане",
            "autor": 1,
            "description": "Edited «Сказка о царе Салтане» − книга, написанная великим мастером русского слова. Книга рассказывает о женитьбе царя Салтана и дальнейшем появлении на свет его сына по имени князь Гвидон. Из-за козней родных теток Гвидон оказывается на необитаемом острове. Там он встречает могущественную волшебницу, известную как царевна Лебедь.",
            "publish_date": "2023-04-30",
        }
        response = self.client.put("/api/books/1/", data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Edited Сказка о царе Салтане")
        self.assertEqual(len(Book.objects.all()), 1)

    def test_delete_book(self):
        response = self.client.delete("/api/books/1/", HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Book.objects.all()), 0)
