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








