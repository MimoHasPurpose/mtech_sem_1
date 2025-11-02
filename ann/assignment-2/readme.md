q1.
- block-1:[3*3*16]*2
- block-2:[3*3*32]*2
- block-3:[3*3*64]*2
p-1: 
    - b-1-> fc->softmax
    - b-1,2-> fc->softmax
    - b-1,2,3->fc->softmax
    - tank h or relu functions
    - Implement dropout and use 
        -  after convolution layers
        -  between FC Layers
## Deliverables:
1. visualize 10 random images for each class
2. analyze accuracy and loss while adding block 1, b2, b3
3. analyze acc and loss while changing the droupout probability
4. Initialize neural network weights by following 
    1. zero initialization
    2. random initialization
    3. he initialization
    which approach is best and why?
5. report best accuracy with model architecture, and detail analysis of choosing specific hyperparameters
6. Analyze the result of the best model when all the activation functions are removed justify performance drop


Dataset description:
1. 10000 samples
2. 8k training, 2k testing
3. each row of array contains 32x32 color images
4. train key contains a list of 10k numbers containing (0-9)




report link:
https://docs.google.com/document/d/1hv13t6Z8pnjxGR4Sv1eRuCG1cMJue-PaS6brLM96l_0/edit?usp=sharing



references:
1. https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html



