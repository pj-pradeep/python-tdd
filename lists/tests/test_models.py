from django.test import TestCase

from lists.models import Item, List
from django.core.exceptions import ValidationError


class ItemModelTest(TestCase):

    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')


    def test_item_is_related_to_list(self):
        new_list = List.objects.create()
        item = Item()
        item.list = new_list
        item.save()
        self.assertIn(item, new_list.item_set.all())


    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()


    def test_duplicate_items_are_invalid(self):
        new_list = List.objects.create()
        Item.objects.create(list=new_list, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=new_list, text='bla')
            item.full_clean()


    def test_CAN_save_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean()   # should not raise


    def test_list_ordering(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='item 1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='item 3')
        self.assertEqual(
            list(Item.objects.all()),
            [item1, item2, item3]
        )


    def test_string_representation(self):
        item = Item(text='test item')
        self.assertEqual(str(item), 'test item')


class ListModelTest(TestCase):

    def test_get_absolute_url(self):
        new_list = List.objects.create()
        self.assertEqual(new_list.get_absolute_url(), f'/lists/{new_list.id}/')