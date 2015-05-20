from django.test import TestCase
from django.contrib.auth.models import User
from rpg_base.models import *


class DndClassTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


class RaceTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


class CharacterTemplateTestCase(TestCase):

    def setUp(self):
        # Race
        self.race1 = Race(name='Hooman')
        self.race1.save()

        # User
        self.test_user = User(username="brenttest",  password="testpassword", email='brent.mitton+testcase@gmail.com')
        self.test_user.save()

        # Campaign
        self.campaign1 = Campaign(name='Rise of the Testlords', description='tests are cool', user=self.test_user)
        self.campaign1.save()

        # CharacterTemplate
        self.template1 = CharacterTemplate(name='BrentTest', race=self.race1)
        self.template1.save()

        # HitDie
        self.hd1 = HitDie(num=1, die=4, mod=0, character_template=self.template1)
        self.hd1.save()

    def tearDown(self):
        pass

    def test_create_characters(self):
        """
        Test that the create_characters() function on the character template
        works as expected.
        """
        characters = self.template1.create_characters(campaign=self.campaign1)
        self.assertEqual(1, len(characters))
        self.assertEqual(characters[0].name, 'BrentTest')

        # args - campaign, name='NolanTest'
    def test_create_characters__with_name(self):
        characters = self.template1.create_characters(campaign=self.campaign1, name='NolanTest')
        self.assertEqual(1, len(characters))
        self.assertEqual(characters[0].name, 'NolanTest')

        # args - campaign, num=100
    def test_create_characters__100_characters(self):
        characters = self.template1.create_characters(campaign=self.campaign1, num=100)
        self.assertEqual(100, len(characters))
        for i in range(len(characters)):
            self.assertEqual(characters[i].name, 'BrentTest %s' % (i + 1))

    def test_create_characters__100_characters_with_name(self):
        characters = self.template1.create_characters(campaign=self.campaign1, num=100, name='NolanTest')
        self.assertEqual(100, len(characters))
        for i in range(len(characters)):
            self.assertEqual(characters[i].name, 'NolanTest %s' % (i + 1))

    def test_create_characters__character_is_encounter_only(self):
        characters = self.template1.create_characters(campaign=self.campaign1)

        for character in characters:
            self.assertTrue(character.encounter_only)

    def test_create_characters__types_are_good(self):
        characters = self.template1.create_characters(campaign=self.campaign1)
        for character in characters:
            self.assertEqual(character.type, 'EN')

        characters = self.template1.create_characters(campaign=self.campaign1, num=10, type='AL')
        for character in characters:
            self.assertEqual(character.type, 'AL')

        characters = self.template1.create_characters(campaign=self.campaign1, num=10, type='NT')
        for character in characters:
            self.assertEqual(character.type, 'NT')

        characters = self.template1.create_characters(campaign=self.campaign1, num=10, type='PL')
        for character in characters:
            self.assertEqual(character.type, 'PL')

    def test_create_characters__hp_gt_0(self):
        characters = self.template1.create_characters(campaign=self.campaign1)
        for character in characters:
            print character.hp
            self.assertTrue(character.hp > 0)

class CharacterTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass



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

        # 1d4 should be in [1, 4]
        d4 = HitDie(die=4)
        rolls = []
        for i in range(1000):
            rolls.append(d4.roll())

        self.assertTrue(all(n >= 1 for n in rolls))
        self.assertTrue(all(n <= 4 for n in rolls))

        # d12+10 should be in [11, 22]
        d12_plus10 = HitDie(die=12, mod=10)
        rolls = []
        for i in range(1000):
            rolls.append(d12_plus10.roll())

        self.assertTrue(all(n >= 1 for n in rolls)) # TODO Should this be >= 11 ?
        self.assertTrue(all(n <= 22 for n in rolls))

        # 4d8 should be in [4, 32]
        four_d8 = HitDie(die=8, num=4)
        rolls = []
        for i in range(1000):
            rolls.append(four_d8.roll())

        self.assertTrue(all(n >= 4 for n in rolls))
        self.assertTrue(all(n <= 32 for n in rolls))

        # 3d12+7 should be in [7, 51]
        four_d12_plus3 = HitDie(num=3, die=12, mod=7)
        rolls = []
        for i in range(1000):
            rolls.append(four_d12_plus3.roll())

        self.assertTrue(all(n >= 7 for n in rolls))
        self.assertTrue(all(n <= 51 for n in rolls))

        # d6-3 should be in [1, 3]
        d6_minus3 = HitDie(die=6, mod=-3)
        rolls = []
        for i in range(1000):
            rolls.append(d6_minus3.roll())

        self.assertTrue(all(n >= 1 for n in rolls))
        self.assertTrue(all(n <= 3 for n in rolls))




