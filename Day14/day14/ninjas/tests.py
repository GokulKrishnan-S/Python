from django.test import TestCase
from django.urls import reverse
from .models import Developer, Skill
from .views import level

# Create your tests here.
class HttpResponseTests(TestCase):
    def test_returns_status_code_200_for_index(self):
        '''
        Test to check if index returns 200
        '''
        url = reverse('ninjas:index')
        response = self.client.get(url)
        message = "Response status code 200"
        self.assertIs(response.status_code, 200, message)

    def test_returns_status_code_200_for_details(self):

        dev = Developer(name='Latte', experience=5, country='US')
        dev.save()
        url = reverse('ninjas:details', args=(dev.id,))
        response = self.client.get(url)
        message = "Response status code 200"
        self.assertIs(response.status_code, 200, message) 

class ModelandViewTests(TestCase):
    def test_creates_developer(self):
        dev = Developer(name='Latte', experience=5, country='US')
        dev.save()
        self.assertIs(dev.name, 'Latte', 'Test - Developer created')

    def test_creates_skill_for_developer(self):
        dev = Developer(name='Latte', experience=5, country='US')
        dev.save()
        skill = dev.skill_set.create(name='Python', level=4)
        self.assertIs(skill.name, 'Python', 'Test - Skill for Developer created')    


