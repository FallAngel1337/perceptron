class Perceptron():
    def __init__(self, inputs, weights, bias=3):
        self.inputs = inputs
        self.weights = weights
        self.bias = bias

    def from_perceptrons(perceptrons, weights, bias=3):
        inputs = []
        weights = weights
        bias = bias

        for perceptron in perceptrons:
            inputs.append(perceptron.activate_function())
        
        return Perceptron(inputs, weights, bias)

    def activate_function(self):
        inputs = self.inputs
        weights = self.weights
        bias = self.bias

        assert(len(inputs) > 0 and len(weights) > 0)

        if len(inputs) == 1:
            inputs.append(inputs[0])

        if len(inputs) > len(weights) and len(weights) == 1:
            for _ in range(len(weights)):
                weights.append(weights[0])

        prod = 0
        for i in range(len(inputs)):
            prod += inputs[i] * weights[i]
        
        return 1 if prod + bias > 0 else 0