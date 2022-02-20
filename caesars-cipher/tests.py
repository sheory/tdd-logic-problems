from unittest import TestCase

from caesars_cipher import encrypt
from caesars_cipher import decrypt

class CaeserCipher(TestCase):
    def test_should_return_def_letters_when_input_is_abc(self):
        _input = 'abc'
        expected_output = 'def'

        self.assertEqual(encrypt(_input), expected_output)

    def test_should_return_abc_letters_when_input_is_xyz(self):
        _input = 'xyz'
        expected_output = 'abc'

        self.assertEqual(encrypt(_input), expected_output)

    def test_should_return_abc_letters_when_input_is_def(self):
        _input = 'def'
        expected_output = 'abc'

        self.assertEqual(decrypt(_input), expected_output)

    def test_should_return_xyz_letters_when_input_is_abc(self):
        _input = 'abc'
        expected_output = 'xyz'

        self.assertEqual(decrypt(_input), expected_output)


