from perceptron import Perceptron

def nand_gate(x1, x2):
    return Perceptron([x1, x2], [-2]).stepf()

def not_gate(x1):
    return Perceptron([x1, x1], [-2]).stepf()

def and_gate(x1, x2):
    return not_gate(nand_gate(x1, x2))

def or_gate(x1, x2):
    p1 = Perceptron([x1, x1], [-2]).stepf()
    p2 = Perceptron([x2, x2], [-2]).stepf()
    return Perceptron([p1, p2], [-2]).stepf()

def nor_gate(x1, x2):
    return not_gate(or_gate(x1, x2))