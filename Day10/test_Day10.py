'''
Python Day10 pyTest
'''

import pytest
import requests

def test_get_groceries_responds_200():
     response = requests.get("http://localhost:5000/veggies")
     assert response.status_code == 200

def test_post_groceries_responds_201():
     response = requests.post("http://localhost:5000/veggies", json={"veggie_name":"raddish","quantity":10})
     assert response.status_code == 201


def test_put_groceries_responds_202():
     response = requests.put("http://localhost:5000/veggies/carrot", json={"quantity":7})
     assert response.status_code == 202


def test_delete_groceries_responds_200():
     response = requests.delete("http://localhost:5000/veggies/carrot")
     assert response.status_code == 200