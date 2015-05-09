from django.test import TestCase
from django.contrib.auth.models import User
from rpg_base.models import *


class EncounterTestCase(TestCase):
    def setUp(self):
        # User
        self.test_user = User(username="brenttest",  password="testpassword", email='brent.mitton+testcase@gmail.com')
        self.test_user.save()

        # Campaign
        self.campaign1 = Campaign(name='Rise of the Testlords', description='tests are cool', user=self.test_user)
        self.campaign1.save()

        # Encounter
        self.encounter1 = Encounter(name='Kill the Testlord!', campaign=self.campaign1)

    def tearDown(self):
        pass

    def test_start(self):
        pass

    def test_end(self):
        pass
