
from django.test import TestCase, Client
from django.urls import reverse


class TestDwsSite(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_home_page(self):
        response = self.client.get(reverse(""))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='index.html')

    def test_get_show_product_category(self):
        response = self.client.get(reverse("<slug:category_slug>/"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='index.html')

    def test_get_detail_product(self):
        response = self.client.get(reverse(""))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='detail_product.html')

    def test_get_payment(self):
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='payment.html')

    def test_get_payment(self):
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='payment.html')

    def test_get_about_us(self):
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='about_us.html')

    def test_get_delivery(self):
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='delivery.html')

    def test_get_blog(self):
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='blog.html')