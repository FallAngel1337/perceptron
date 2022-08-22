class Perceptron():
    def __init__(self, inputs, weights, bias=0):
        if len(inputs) != len(weights):
            print('Number of inputs must match the number of weights')
            return None

        self.inputs = inputs
        self.weights = weights
        self.bias = bias
        
    def activate_function(self):
        prod = 0
        for i in range(len(self.inputs)):
            prod += self.inputs[i] * self.weights[i]
            
        return 1 if prod + self.bias > 0 else 0