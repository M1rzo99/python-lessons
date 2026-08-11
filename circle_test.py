
# Matnlardan farqli ravishda, sonlarni taqqoslash uchun assertAlmostEqual() metodidan foydalanamiz. Bu metod, ikki sonni nuqtadan keyin 7 xonagacha aniqlikda tekshiradi:

import unittest
from circle import getPerimetr,getArea

class CircleTest(unittest.TestCase):
    def test_are(self):
        self.assertAlmostEqual(getArea(10),314.159)
        self.assertAlmostEqual(getArea(5),78.53975)
        
    def test_perimetr(self):
        self.assertAlmostEqual(getPerimetr(10),62.8318)
        self.assertAlmostEqual(getPerimetr(5),31.4159)
unittest.main()