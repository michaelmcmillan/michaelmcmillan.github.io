from unittest import TestCase, skip
from merger import merge

class TestRightPad(TestCase):
    
    def test_two_strings_can_be_merged_white_separation(self):
        first_string = 'hello world. how are you?'
        second_string = 'hi there. i am fine'
        merged = merge(first_string, second_string, 40)
        self.assertEqual(merged, 'hello world. how are you?               hi there. i am fine')

    def test_linebreaks_are_also_separated_across_each_string(self):
        first_string = 'hello world.\nhow are you?'
        second_string = 'hi there.\ni am fine.'
        merged = merge(first_string, second_string, 40)
        self.assertEqual(merged, 'hello world.                            hi there.\n' + \
                                 'how are you?                            i am fine.')

    def test_separation_is_relative_to_the_line_ending_in_first_string(self):
        first_string = 'hello world, long time no see!\nhow are you?'
        second_string = 'hi there.\ni am fine.'
        merged = merge(first_string, second_string, 40)
        self.assertEqual(merged, 'hello world, long time no see!          hi there.\n' + \
                                 'how are you?                            i am fine.')

    def test_works_even_if_there_are_more_lines_in_first_sentence(self):
        first_string = 'hello world, long time no see!\nhow are you?\ni am glad to hear that.'
        second_string = 'hi there.\ni am fine.'
        merged = merge(first_string, second_string, 40)
        self.assertEqual(merged, 'hello world, long time no see!          hi there.\n' + \
                                 'how are you?                            i am fine.\n' + \
                                 'i am glad to hear that.')

    def test_works_even_if_there_are_more_lines_in_second_sentence(self):
        first_string = 'hello world, long time no see!\nhow are you?'
        second_string = 'hi there.\ni am fine.\nthanks for asking.'
        merged = merge(first_string, second_string, 40)
        self.assertEqual(merged, 'hello world, long time no see!          hi there.\n' + \
                                 'how are you?                            i am fine.\n' + \
                                 '                                        thanks for asking.')
