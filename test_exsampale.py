# import unittest
#
# from django.template.defaultfilters import upper
#
#
# def apper(string: str):
#     return string.upper()
#
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         expected: str = 'FOO'
#         test_value = upper('foo')
#         self.assertEqual(expected, test_value)
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())