import os
from django.test import TestCase
from partner.util import load_choices

HERE = os.path.abspath(os.path.dirname(__file__))

# Create your tests here.


class TestChoiceLoader(TestCase):

    def test_choices_are_loaded(self):
        choices = load_choices(os.path.join(HERE, 'states.txt'), True)
        self.assertEqual(len(choices), 50)
        self.assertIn(('OR', 'Oregon'), choices)
