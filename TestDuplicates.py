import ddt
import unittest

from Duplicates import Duplicates

@ddt.ddt
class TestDuplicates(unittest.TestCase):

    def setUp(self):
        self.Duplicates = Duplicates()

    @ddt.data(
            ('мама мыла раму', ['м', 'а', ' ']), # 1 cyrillic
            ('  abcc', [' ', 'c']), # 2 string starts with two spaces
            (',kk,', [',', 'k']),    # 3 начинается с запятой
            ('', []),         # 4 empty string input
            (' ', []),         # 5 one character, input space
            ('  ', [' ']),      # 6 input two spaces
            ('xyzz  ', ['z', ' ']), # 7 input two spaces at the end of the strings
            ('0', []),         # 8 input 0
            ('00', ['0']),       # 9 input two zeros
            ('null', ['l']),     # 10 input 'null'
            ('off-white shirt', ['f', 'h', 'i', 't']),   # 11 hyphenated word

            ('Queen Elizabeth the Second,'
             'by the Grace of God Queen of this Realm and of Her other Realms and Territories,'
             ' Head of the Commonwealth, Defender of the Faith',
             ['Q', 'u', 'e', 'n', ' ', 'l', 'i', 'a', 'b', 't', 'h', 'c',
              'o', 'd', ',', 'G', 'r', 'f', 's', 'R', 'm', 'H']),       # 12 many words, different case letters

            ('qwertyQ', []), # 13 lowercase and uppercase letters
            ('Qwertyq', []), # 14 uppercase and lowercase letters
            ('12345678901', ['1']), # 15 digits
            ('!@#$%^&*()-=_+[]{};:"|/?.>,<`~!\!!!', ['!']), # 16 special characters
            ("''", ["'"]), # 17 single quotes
            ('asdgha\tdfghj\t', ['a', 'd', 'g', 'h', '\t']), # 18 test escape character
            ('8🐒🐒', ['🐒']) # 19 emoji
    )

    def test_FindDuplicates(self, case):
        initialString, expectedOutputArray = case
        self.assertEqual(self.Duplicates.FindDuplicates(initialString), expectedOutputArray)

if __name__ == '__main__':
    unittest.main()