class Perceptron():      
    def activate_function(inputs, weights, bias=3):
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