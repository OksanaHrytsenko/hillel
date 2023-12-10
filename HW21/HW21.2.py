import unittest


def formatted_name(first_name, last_name, middle_name=''):
   if len(middle_name) > 0:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
   else:
       full_name = first_name + ' ' + last_name
   return full_name.title()


class TestFormattedName(unittest.TestCase):

    def test_no_middle_name(self):
        full_name = formatted_name('John', 'Doe')
        self.assertEqual(full_name, 'John Doe')

    def test_with_middle_name(self):
        full_name = formatted_name('John', 'Doe', 'Smith')
        self.assertEqual(full_name, 'John Smith Doe')

    def test_middle_name_empty(self):
        full_name = formatted_name('John', 'Doe', '')
        self.assertEqual(full_name, 'John Doe')

    def test_middle_name_with_spaces(self):
        full_name = formatted_name('John', 'Doe', '   Smith   ')
        self.assertEqual(full_name, 'John Smith Doe')


if __name__ == '__main__':
    unittest.main()

