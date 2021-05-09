import metre_detector as met
from unittest import TestCase

class TestMetreDetection(TestCase):

    def test_adjust_syllables_for_metre_detection(self):
        self.assertEqual(met.adjust_syllables_for_metre_detection(met.syllabify_verse("από αγάλματα και εικόνες")),
                         ["α", "πό", "α", "γάλ", "μα", "τα", "καιει", "κό", "νες"], "Splitting was wrong")
        self.assertEqual(met.adjust_syllables_for_metre_detection(met.syllabify_verse("σε γνωρίζω από την κόψη")),
                         ["σε", "γνω", "ρί", "ζωα", "πό", "την", "κό", "ψη"], "Splitting was wrong")
        self.assertEqual(met.adjust_syllables_for_metre_detection(met.syllabify_verse("Την είδα την Ξανθούλα,")),
                         ["την", "εί", "δα", "την", "ξαν", "θού", "λα,"], "Splitting was wrong")
        self.assertNotIn("", met.adjust_syllables_for_metre_detection(met.syllabify_verse("Την είδα την Ξανθούλα,")),
                         "Empty strings are not allowed in the list")

    def test_is_stressed(self):
        self.assertEqual(met.is_stressed("α"), False, "Syllable was recognized as stressed even though it is unstressed")
        self.assertEqual(met.is_stressed("ρί"), True, "Syllable was recognized as unstressed even though it is stressed")

    def test_detect_stress(self):
        self.assertEqual(met.detect_stress(["α", "πό", "α", "γάλ", "μα", "τα", "καιει", "κό", "νες"]),
                         ["u", "s", "u", "s", "u", "u", "u", "s", "u"], "The stress detection was incorrect")
        self.assertEqual(len(met.detect_stress(["α", "πό", "α", "γάλ", "μα", "τα", "καιει", "κό", "νες"])),
                         len(["u", "s", "u", "s", "u", "u", "u", "s", "u"]), "The number of syllables does is not "
                                                                             "equal to the number of elements in the "
                                                                             "stress list")
        self.assertNotIn("", met.detect_stress(["την", "εί", "δα", "την", "ξαν", "θού", "λα,"]),
                         "Empty strings are not allowed in the list")








