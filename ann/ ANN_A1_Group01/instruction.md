
- report ANN_A1_GroupXX.pdf
- The report must contain the google drive link of the folder where you upload the plots,
    output images, saved model etc. Report all your solutions, results and outputs in
    ANN_A1_GroupXX.pdf. (XX denotes your group number)
- numpy, scipy, matplotlib only
- question
    - q1: implement forward and backprop algorithm to train a ANN on cifar 10 dataset (https://www.cs.toronto.edu/~kriz/cifar.html)
      - argument to ya function would be no of layers and no of nodes
      - sigmoid activation function in each layer
      - softmax in output layer
      - construct following neural architectures:
        - 1 hidden layer(100 units)
        - 3 hidden layer(100,50,50 units)
      - implement forward and backward propagation use this to implement 2 archs and test on cifar 10 report accuracy as evaluation metric
      - save weights of best models
    - q2: diagnoes if model is overfit or underfit and
      - plt and graphs showing well trained model
      - proper justification of challenges and counter-measures
    - q3: repeat part a, b with relu
    - q4: implement part a using sklearn, report accuracy as compared our own network , explain reason for observed difference in accuracy
  