from django.test import TestCase
from django.contrib.auth.models import User
from rpg_base.models.character import *
from rpg_base.models.campaign import Campaign



class CharacterTemplateTestCase(TestCase):

    def setUp(self):

        # race needed to satisfy character requirements
        self.race1 = Race(name='Hooman')
        self.race1.save()

        self.test_user = User(username="brenttest", password="testpassword",
                              email='brent.mitton+testcase@gmail.com')
        self.test_user.save()

        self.campaign1 = Campaign(name='Rise of the Testlords',
                                  description='tests are cool',
                                  user=self.test_user)
        self.campaign1.save()

    def tearDown(self):
        pass

    def test_create_characters(self):
        """
        Test that the create_characters() function on the character template
        works as expected
        """
        char_template = CharacterTemplate(name='BrentTest',
                                          race=self.race1)
        char_template.save()

        # no arguments provided to create_character() (besides campaign)
        characters = char_template.create_characters(campaign=self.campaign1)
        self.assertEqual(1, len(characters))
