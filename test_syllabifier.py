import syllabifier as syl
from unittest import TestCase


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

    def test_output_syllabify_token(self):
        self.assertIsInstance(syl.syllabify_token("αεροπλάνο"), str, "Required output type is string!")

    def test_syllabify_token(self):
        self.assertEqual(syl.syllabify_token("αεροπλάνο"), "α ε ρο πλά νο", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("άστρο"), "ά στρο", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("φτάνω"), "φτά νω", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("οχιά"), "ο χιά", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("βοήθα"), "βο ή θα", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("βόηθα"), "βόη θα", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("ευτυχία"), "ευ τυ χί α", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("βαθμούς"), "βαθ μούς", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("φίλτατος"), "φίλ τα τος", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("μυαλωμένος"), "μυα λω μέ νος", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("δουλειά"), "δου λειά", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("δουλεία"), "δου λεί α", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("αργαλειού"), "αρ γα λειού", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("παιδιών"), "παι διών", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("αέναη"), "α έ ναη", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("αηδόνι"), "αη δό νι", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("αΰμνηστος"), "α ΰ μνη στος", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("εκπτώσεις"), "εκ πτώ σεις", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("τριαντάφυλλο"), "τρια ντά φυλ λο", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("πολιορκημένοι"), "πο λιορ κη μέ νοι", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("όμορφος"), "ό μορ φος", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("θάλασσα"), "θά λασ σα", "Syllabification was wrong!")
        self.assertEqual(syl.syllabify_token("ασπίδα"), "α σπί δα", "Syllabification was wrong!")

    def test_output_syllabify_verse(self):
        self.assertIsInstance(syl.syllabify_verse("από αγάλματα και εικόνες"), list, "Required output type is list!")
        self.assertIsInstance(syl.syllabify_verse("σε γνωρίζω από την κόψη"), list, "Required output type is list!")

    def test_syllabify_verse(self):
        self.assertEqual(syl.syllabify_verse("από αγάλματα και εικόνες"),
                         ["α", "πό", "α", "γάλ", "μα", "τα", "και", "ει", "κό", "νες"], "Splitting was wrong")
        self.assertEqual(syl.syllabify_verse("σε γνωρίζω από την κόψη"),
                         ["σε", "γνω", "ρί", "ζω", "α", "πό", "την", "κό", "ψη"], "Splitting was wrong")
        self.assertEqual(syl.syllabify_verse("Την είδα την Ξανθούλα,"),
                         ["την", "εί", "δα", "την", "ξαν", "θού", "λα,"], "Splitting was wrong")
        self.assertNotIn("", syl.syllabify_verse("Την είδα την Ξανθούλα,"), "Empty strings are not supposed to be in "
                                                                            "the list")
