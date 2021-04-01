import syllabifier as syl
from unittest import TestCase, main


class TestSyllabification(TestCase):

    def test_output_is_monosyllable(self):
        self.assertIsInstance(syl.is_monosyllable("που"), bool, "Required output type is bool!")
        self.assertIsInstance(syl.is_monosyllable("ποτέ"), bool, "Required output type is bool!")

    def test_is_monosyllable(self):
        monosyllable_words = ["φλερτ", "μπλουζ", "μια", "δυό", "μπα",  "που", "τρεις", "γκολφ", "ποιος", "φλας", "μποξ",
                              "σνομπ", "βρε", "αχ", "δω", "πως", "πού", "να", "βγω", "γκρι", "θεια", "γιε", "γιοι",
                              "πώς"]
        polysyllable_words = ["αεροπλάνο", "σημαία", "μπλούζα", "μαία", "σχολειού", "μία", "θεία", "ελεύθεροι", "αγάπη",
                              "άστρων", "ευτυχίας", "ελπίς", "φιλάει", "στεναχώρια", "κλάψει", "βήματα", "ήλιος",
                              "αδελφών", "φωτιά", "υιέ"]
        for word in monosyllable_words:
            self.assertEqual(syl.is_monosyllable(word), True, f"The monosyllable word {word} is not recognized as "
                                                              f"monosyllable!")
        for word in polysyllable_words:
            self.assertEqual(syl.is_monosyllable(word), False, f"The polysyllable word {word} is not recognized as "
                                                               f"polysyllable!")

    def test_output_syllabify_token_while(self):
        self.assertIsInstance(syl.syllabify_token_while("αεροπλάνο"), str, "Required output type is string!")

    def test_syllabify_token_while(self):
        self.assertEqual(syl.syllabify_token_while("αεροπλάνο"), "α ε ρο πλά νο", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("άστρο"), "ά στρο", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("φτάνω"), "φτά νω", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("οχιά"), "ο χιά", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("βοήθα"), "βο ή θα", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("βόηθα"), "βόη θα", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("ευτυχία"), "ευ τυ χί α", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("βαθμούς"), "βαθ μούς", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("φίλτατος"), "φίλ τα τος", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("μυαλωμένος"), "μυα λω μέ νος", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("δουλειά"), "δου λειά", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("δουλεία"), "δου λεί α", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("αργαλειού"), "αρ γα λειού", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("παιδιών"), "παι διών", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("αέναη"), "α έ ναη", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("αηδόνι"), "αη δό νι", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("αΰμνηστος"), "α ΰ μνη στος", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("εκπτώσεις"), "εκ πτώ σεις", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("τριαντάφυλλο"), "τρια ντά φυλ λο", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("πολιορκημένοι"), "πο λιορ κη μέ νοι", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("όμορφος"), "ό μορ φος", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("θάλασσα"), "θά λασ σα", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token_while("ασπίδα"), "α σπί δα", "Syllabification was wrong!")

