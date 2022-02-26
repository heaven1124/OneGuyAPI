import random

import requests
import unittest
from unittest import TestCase


class UserTestCase(TestCase):
    def test_01_all_user(self):
        url = 'http://localhost:8080/user/all'
        resp = requests.get(url)
        user_list = resp.json().get('data')
        user = random.choice(user_list)

        self.user_id = user['id']
        print('------当前用户为----', user['name'])
