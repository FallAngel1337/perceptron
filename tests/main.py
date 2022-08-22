import sys, os
# Workaround for modudule visibility
sys.path.append(os.path.abspath("../"))

import unittest
import perceptron_gates;

class TestPerceptronGates(unittest.TestCase):
    def test_nand_gate(self):
        self.assertEqual(perceptron_gates.nand_gate(0, 0), 1)
        self.assertEqual(perceptron_gates.nand_gate(0, 1), 1)
        self.assertEqual(perceptron_gates.nand_gate(1, 0), 1)
        self.assertEqual(perceptron_gates.nand_gate(1, 1), 0)

    def test_not_gate(self):
        self.assertEqual(perceptron_gates.not_gate(0), 1)
        self.assertEqual(perceptron_gates.not_gate(1), 0)

    def test_and_gate(self):
        self.assertEqual(perceptron_gates.and_gate(0, 0), 0)
        self.assertEqual(perceptron_gates.and_gate(0, 1), 0)
        self.assertEqual(perceptron_gates.and_gate(1, 0), 0)
        self.assertEqual(perceptron_gates.and_gate(1, 1), 1)

    def test_or_gate(self):
        self.assertEqual(perceptron_gates.or_gate(0, 0), 0)
        self.assertEqual(perceptron_gates.or_gate(0, 1), 1)
        self.assertEqual(perceptron_gates.or_gate(1, 0), 1)
        self.assertEqual(perceptron_gates.or_gate(1, 1), 1)

    def test_not_gate(self):
        self.assertAlmostEqual(perceptron_gates.nor_gate(0, 0), 1)
        self.assertAlmostEqual(perceptron_gates.nor_gate(0, 1), 0)
        self.assertAlmostEqual(perceptron_gates.nor_gate(1, 0), 0)
        self.assertAlmostEqual(perceptron_gates.nor_gate(1, 1), 0)

if __name__ == '__main__':
    unittest.main()
