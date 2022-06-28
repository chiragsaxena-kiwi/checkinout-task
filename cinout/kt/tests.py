import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class RegistrationTestcas(APITestCase):
  
      def test_abaout_page_status_code(self):
          response = self.client.get(reverse("profile"))
          self.assertEqual(response.status_code, 200) 

      
      def test_abaout_page_status_code1(self):
          response = self.client.get(reverse("signup"))
          self.assertEqual(response.status_code, 200) 

      
      def test_abaout_page_status_code2(self):
          response = self.client.get(reverse("checkin"))
          self.assertEqual(response.status_code, 200)  

from django.test import SimpleTestCase
from django.urls import reverse,resolve
from kt.views import checkinView

class TestingUrls(SimpleTestCase):
    """testing the urls"""
    def test_login(self):
        """testing the login url"""
        url = reverse('checkin')
        self.assertEqual(resolve(url).func.view_class, checkinView)

    from datetime import datetime
from rest_framework.test import APITestCase

# project import
from django.core.management import call_command
from kt.models import Signup, Term



class CreateSimpleUserTest(APITestCase):
    """
    create user for test cases
    """
    # set up for test cases

    # def setUp(self):
    #     self.user=User.objects.create(user_name='user details edit')
    #     self.assertEqual(str(self.user),'user details edit')

#model test case
    def test_correct_term_created(self):
        self.term=Term.objects.create(details='test') 
       # self.assertEquals(str(self.term),'test')



       
    
    
