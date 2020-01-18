from django.test import TestCase
from django.shortcuts import get_object_or_404
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

    def test_say_hello_page(self):
        response = self.client.get("/message")
        self.assertEqual(response.content, b"Hello World")

    def test_post_create_an_item(self):
        # create an item with POST
        self.client.post("/add", {"name": "Create a test"})
        # get that item
        item = get_object_or_404(Item,pk=1)
        self.assertEqual(item.done, False)
    
    def test_post_edit_an_item(self):
        # create an item in database
        item = Item(name="Create a test")
        item.save()
        id = item.id
        # edit the item with POST
        self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        # get that item
        item = get_object_or_404(Item, pk=id)
        self.assertEqual("A different name", item.name)

    def test_toggle_status(self):
        item = Item(name="Create a test")
        item.save()
        id = item.id
        # toggle status with POST
        self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)