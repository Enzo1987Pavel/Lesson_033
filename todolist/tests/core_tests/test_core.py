import json

import pytest
from django.urls import reverse

from core import serializers


@pytest.mark.django_db
def test_create(client):
    response = client.post(reverse("signup"),
                           data={"username": "newtestuser",
                                 "first_name": "testfirst",
                                 "last_name": "testlast",
                                 "email": "email@mail.ru",
                                 "password": "super1Password",
                                 "password_repeat": "super1Password"})

    expected_response = {"username": "newtestuser",
                         "first_name": "testfirst",
                         "last_name": "testlast",
                         "email": "email@mail.ru", }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_login(client, new_user):
    response = client.post(reverse("login_user"),
                           data=json.dumps({"username": "testname",
                                            "password": "SuperPassword12345"}),
                           content_type="application/json")

    assert response.status_code == 200


@pytest.mark.django_db
def test_retrieve(auth_client, new_user):
    response = auth_client.get(reverse("profile"))
    expected_response = serializers.ProfileSerializer(instance=new_user).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_update(auth_client, new_user):
    response = auth_client.put(reverse("profile"),
                               data={"username": "testupdateusername",
                                     "first_name": "testfirst",
                                     "last_name": "testlast",
                                     "email": "testupdate@mail.ru"})

    assert response.status_code == 200
    assert response.data == {"id": new_user.id,
                             "username": "testupdateusername",
                             "first_name": "testfirst",
                             "last_name": "testlast",
                             "email": "testupdate@mail.ru"}
