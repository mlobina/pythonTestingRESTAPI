from putting_folder import put_folder
import pytest
import requests


def test_put_folder():
    response = put_folder('test')
    assert response == True

