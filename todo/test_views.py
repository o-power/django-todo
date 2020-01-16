from django.test import TestCase
from .models import Item

class TestViews(TestCase):
    # method has to start with test_
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
    
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_item_page(self):
        item =  Item(name="Create a template test")
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_item_page_for_item_that_does_not_exist(self):
        # test database is empty?
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)