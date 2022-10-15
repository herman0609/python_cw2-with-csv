import unittest


class TestCheckKey(unittest.TestCase):

    def test_check_key(self):
        from file01 import check_key
        with self.subTest(1):
            a = check_key(-1)
            self.assertFalse(a)
        with self.subTest(2):
            b = check_key(0)
            self.assertTrue(b)
        with self.subTest(3):
            c = check_key(1)
            self.assertTrue(c)
        with self.subTest(4):
            d = check_key(50)
            self.assertTrue(d)
        with self.subTest(5):
            e = check_key(94)
            self.assertTrue(e)
        with self.subTest(6):
            f = check_key(95)
            self.assertFalse(f)
        with self.subTest(7):
            g = check_key("a")
            self.assertFalse(g)

    def test_check_upper_lower(self):
        from file01 import check_upper_lower
        with self.subTest(1):
            a = check_upper_lower("The quick Brown Fox!")
            self.assertListEqual(a, [3, 13])
        with self.subTest(2):
            b = check_upper_lower("Khoor#Zruog#=,")
            self.assertListEqual(b, [2, 8])
        with self.subTest(3):
            c = check_upper_lower("012345")
            self.assertListEqual(c, [0, 0])

    def test_encrypt_decrypt_string(self):
        from file01 import encrypt_decrypt_string
        with self.subTest(1):
            a = encrypt_decrypt_string("Hello World :)")
            self.assertMultiLineEqual(a, "Khoor#Zruog#=,")
        with self.subTest(2):
            b = encrypt_decrypt_string("Khoor#Zruog#=,", 3, 2)
            self.assertMultiLineEqual(b, "Hello World :)")
        with self.subTest(3):
            c = encrypt_decrypt_string("Khoor#Zruog#=,", option=2)
            self.assertMultiLineEqual(c, "Hello World :)")
        with self.subTest(4):
            d = encrypt_decrypt_string("Hello World :)", key=100)
            self.assertMultiLineEqual(d, "Invalid key!")
        with self.subTest(5):
            e = encrypt_decrypt_string("Hello World :)", option=4)
            self.assertMultiLineEqual(e, "Invalid option!")

    def test_count_words_in_file(self):
        from file01 import count_words_in_file
        with self.subTest(1):
            a = count_words_in_file("test1.txt")
            self.assertDictEqual(a, {'HELLO': 1, 'WORLD': 2, 'HOW': 1,
                                     'ARE': 1, 'YOU': 1, 'DOING': 1,
                                     'I': 1, 'LOVE': 1, 'THIS': 1})
        with self.subTest(2):
            b = count_words_in_file("test2.txt")
            self.assertDictEqual(b, {'TEST': 3, 'ONE': 2,
                                     'TWO': 1, 'THREE': 1})
        with self.subTest(3):
            c = count_words_in_file("test3.txt")
            self.assertMultiLineEqual(c, "Wrong file or file path")

    def test_summarise_data(self):
        from file01 import summarise_data
        with self.subTest(1):
            a = summarise_data("traffic_data.txt", 0)
            self.assertListEqual(a, [13096, 6493, 471876, 50, 9437.52])
        with self.subTest(2):
            b = summarise_data("traffic_data.txt", 1)
            self.assertListEqual(b, [11799, 5778, 421298, 50, 8425.96])
        with self.subTest(3):
            c = summarise_data("population_10.txt", 5)
            self.assertListEqual(c, [1371851, 1730, 3327840, 34, 97877.65])
        with self.subTest(4):
            d = summarise_data("population_10.txt", 6)
            self.assertListEqual(d, [1425791, 1878, 4274491, 38, 112486.61])
        with self.subTest(5):
            self.assertRaises(FileNotFoundError, summarise_data,
                              "filenotexist.txt", 0)
