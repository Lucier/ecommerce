# coding=utf-8


from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy

from catalog.models import Product, Category


class ProducListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:produtos_lista')
        self.client = Client()
        self.products = mommy.make('catalog.Product', _quantity=10)


    def tearDown(self):
        Product.objects.all().delete()


    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/produtos_lista.html')



    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('produtos_lista' in response.context)
        produtos_lista = response.context['produtos_lista']
        self.assertEquals(produtos_lista.count(), 10)

    
