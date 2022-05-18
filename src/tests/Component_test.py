import sys
import os
import unittest

sys.path.append(os.path.abspath('..'))
from drawioartisan.template.Component import Component


class ComponentTest(unittest.TestCase):
    def test_returnSelfClosedWithOneChildren(self):
        # Should return right format when dont have children
        comp = Component('1', 0)
        expectedComponent = '<Component 1 />'
        self.assertEqual(comp.genContent(), expectedComponent)
    
    def test_rightFormat(self):
        # Should return right format when have chlidren
        comp1 = Component('1')
        comp2 = Component('2')
        comp1.push(comp2)
        expectedComponentTree = '<Component 1>\n  <Component 2 />\n</Component 1>'
        self.assertEqual(comp1.genContent(), expectedComponentTree)
    
    def test_indentationUpdate(self):
        # Should update the indentation when children are added
        comp1 = Component('1')
        comp2 = Component('2')
        oldIndent = comp2._Component__indentation
        comp1.push(comp2)
        newIndent = comp2._Component__indentation
        self.assertTrue(oldIndent < newIndent)

if __name__ == '__main__':
    unittest.main()
