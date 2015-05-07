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
        self.assertEqual(characters[0].name, 'BrentTest')

        # 100 characters, because lol
        characters = char_template.create_characters(campaign=self.campaign1,
                                                     num=100)
        self.assertEqual(100, len(characters))
        for i in range(len(characters)):
            self.assertEqual(characters[i].name, 'BrentTest %s' % (i + 1))


class HitDieTestCase(TestCase):

    def setUp(self):
        self.char_template = CharacterTemplate(name="TestTemplate")
    def tearDown(self):
        pass

    def test_roll(self):
        """
        Test that Nolan knows how to generate random numbers
        """
        # I don't really know what the best practices are for dealing with
        # random numbers in tests, but this is mine.

        # Roll a d4
        d4 = HitDie(die=4)

        rolls = []
        for i in range(1000):
            rolls.append(d4.roll())

        self.assertTrue(all(n <= 4 for n in rolls))
        self.assertTrue(all(n >= 1 for n in rolls))

        # roll a d12+10
        d12_plus10 = HitDie(die=12, mod=10)
        rolls = []
        for i in range(1000):
            rolls.append(d12_plus10.roll())

        self.assertTrue(all(n <= 22 for n in rolls))
        self.assertTrue(all(n >= 1 for n in rolls))

        # roll four d8
        four_d8 = HitDie(die=8, num=4)
        rolls = []
        for i in range(1000):
            rolls.append(four_d8.roll())

        self.assertTrue(all(n <= 32 for n in rolls))
        self.assertTrue(all(n >= 4 for n in rolls))




