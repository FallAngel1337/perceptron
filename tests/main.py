import sys, os
# Workaround for modudule visibility
sys.path.append(os.path.abspath("../"))

import unittest
from perceptron import Perceptron

class TestPerceptronGates(unittest.TestCase):
    def test_nand_gate(self):
        self.assertEqual(Perceptron.activate_function([0], [-2]), 1)
        self.assertEqual(Perceptron.activate_function([0, 1], [-2]), 1)
        self.assertEqual(Perceptron.activate_function([1, 0], [-2]), 1)
        self.assertEqual(Perceptron.activate_function([1], [-2]), 0)

    def test_not_gate(self):
        self.assertEqual(Perceptron.activate_function([0], [-2]), 1)
        self.assertEqual(Perceptron.activate_function([1], [-2]), 0)

    def test_and_gate(self):
        self.assertEqual(Perceptron.activate_function([
            Perceptron.activate_function([0], [-2])
        ], [-2]), 0)

        self.assertEqual(Perceptron.activate_function([
            Perceptron.activate_function([0, 1], [-2])
        ], [-2]), 0)

        self.assertEqual(Perceptron.activate_function([
            Perceptron.activate_function([1, 0], [-2])
        ], [-2]), 0)

        self.assertEqual(Perceptron.activate_function([
            Perceptron.activate_function([1], [-2])
        ], [-2]), 1)

    def test_or_gate(self):
        x1 = Perceptron.activate_function([0], [-2])
        x2 = Perceptron.activate_function([0], [-2])
        self.assertEqual(Perceptron.activate_function([x1, x2], [-2]), 0)

        x1 = Perceptron.activate_function([0], [-2])
        x2 = Perceptron.activate_function([1], [-2])
        self.assertEqual(Perceptron.activate_function([x1, x2], [-2]), 1)

        x1 = Perceptron.activate_function([1], [-2])
        x2 = Perceptron.activate_function([0], [-2])
        self.assertEqual(Perceptron.activate_function([x1, x2], [-2]), 1)

        x1 = Perceptron.activate_function([1], [-2])
        x2 = Perceptron.activate_function([1], [-2])
        self.assertEqual(Perceptron.activate_function([x1, x2], [-2]), 1)

    def test_nor_gates(self):
        x1 = Perceptron.activate_function([0], [-2])
        x2 = Perceptron.activate_function([0], [-2])
        o = Perceptron.activate_function([x1, x2], [-2])
        self.assertEqual(Perceptron.activate_function([o], [-2]), 1)

        x1 = Perceptron.activate_function([0], [-2])
        x2 = Perceptron.activate_function([1], [-2])
        o = Perceptron.activate_function([x1, x2], [-2])
        self.assertEqual(Perceptron.activate_function([o], [-2]), 0)

        x1 = Perceptron.activate_function([1], [-2])
        x2 = Perceptron.activate_function([0], [-2])
        o = Perceptron.activate_function([x1, x2], [-2])
        self.assertEqual(Perceptron.activate_function([o], [-2]), 0)
        
        x1 = Perceptron.activate_function([1], [-2])
        x2 = Perceptron.activate_function([1], [-2])
        o = Perceptron.activate_function([x1, x2], [-2])
        self.assertEqual(Perceptron.activate_function([o], [-2]), 0)
        

if __name__ == '__main__':
    unittest.main()
