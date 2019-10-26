# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
# from modules.node.HierNode import HierNode
# from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock
from modules.node.block.ImageBlock import ImageBlock as ibk
# from modules.node.block.ListBlock import ListBlock as lbk
# from modules.node.block.YoutubeBlock import YoutubeBlock as ybk
from modules.nodes.web.WebNode import WebNode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Introduction(HierBlock):
    def __init__(self):
        super().__init__("Introduction", [
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/neural_network_fish.png", "Neural Network like a fish"),
            "We have introduced the basic ideas about neuronal networks in the previous chapter of our tutorial.",
            "We pointed out the similarity between neurons and neural networks in biology. We also introduced very small articial neural networks and introduced decision boundaries and the XOR problem.",
            "The focus in our previous chapter had not been on efficiency.",
            "We will introduce a Neural Network class in Python in this chapter, which will use the powerful and efficient data structures of Numpy. This way, we get a more efficient network than in our previous chapter. When we say \"more efficient\", we do not mean that the artificial neural networks encountered in this chaper of our tutorial are efficient and ready for real life usage. They are still quite slow compared to implementations from sklearn for example. The focus is to implement a very basic neural network and by doing this explaining the basic ideas. We want to demonstrate simple and easy to grasp networks.",
            "Ideas like how the signal flow inside of a network works, how to implement weights. how to initialize weight matrices or what activation functions can be used.",
            "We will start with a simple neural networks consisting of three layers, i.e. the input layer, a hidden layer and an output layer.",
        ])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ASimpleArtificialNeuralNetworkStructure(HierBlock):
    def __init__(self):
        super().__init__("A Simple Artificial Neural Network Structure", [
            "You can see a simple neural network structure in the following diagram. We have an input layer with three nodes i1,i2,i3 These nodes get the corresponding input values x1,x2,x3. The middle or hidden layer has four nodes h1,h2,h3,h4. The input of this layer stems from the input layer. We will discuss the mechanism soon. Finally, our output layer consists of the two nodes o1,o2",
            "We have to note that some would call this a two layer network, because they don't count the inputs as a layer.",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/example_network_3_4_2_without_bias.png", "Neuronal Network with 3 input, 4 hidden und 2 output nodes"),
            "The input layer consists of the nodes i1, i2 and i3. In principle the input is a one-dimensional vector, like (2, 4, 11). A one-dimensional vector is represented in numpy like this:",
            cbk(None, """
import numpy as np
input_vector = np.array([2, 4, 11])
print(input_vector)
            """, """
[ 2  4 11]
            """),
            "In the algorithm, which we will write later, we will have to transpose it into a column vector, i.e. a two-dimensional array with just one column:",
            cbk(None, """
import numpy as np
input_vector = np.array([2, 4, 11])
input_vector = np.array(input_vector, ndmin=2).T
print(input_vector, input_vector.shape)
            """, """
[[ 2]
 [ 4]
 [11]] (3, 1)
            """),
        ])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WeightsAndMatrices(HierBlock):
    def __init__(self):
        super().__init__("Weights and Matrices", [
            "Each of the arrows in our network diagram has an associated weight value. We will only look at the arrows between the input and the output layer now.",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weights_input2hidden_example_values.png", "Links/Arrows between input and hidden layer with example values"),
            "The value x1 going into the node i1 will be distributed according to the values of the weights. In the following diagram we have added some example values. Using these values, the input values (Ih1,Ih2,Ih3,Ih4 into the nodes (h1,h2,h3,h4) of the hidden layer can be calculated like this:",
            "$$ Ih_1=0.81*0.5+0.12∗1+0.92∗0.8 $$",
            "$$ Ih_2=0.33∗0.5+0.44∗1+0.72∗0.8 $$",
            "$$ Ih_3=0.29∗0.5+0.22∗1+0.53∗0.8 $$",
            "$$ Ih_4=0.37∗0.5+0.12∗1+0.27∗0.8 $$",
            "Those familiar with matrices and matrix multiplication will see where it is boiling down to. We will redraw our network and denote the weights with wij:",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weights_input2hidden_1.png", "Links/Arrows between input and hidden layer"),
            "In order to efficiently execute all the necessary calaculations, we will arrange the weights into a weight matrix. The weights in our diagram above build an array, which we will call 'weights_in_hidden' in our Neural Network class. The name should indicate that the weights are connecting the input and the hidden nodes, i.e. they are between the input and the hidden layer. We will also abbreviate the name as 'wih'. The weight matrix between the hidden and the output layer will be denoted as \"who\".:",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weight_matrix_input.png", "weight matrix between the input and the hidden layer"),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weight_matrix_hidden.png", "weight matrix between the hidden and the output layer"),
            "Now that we have defined our weight matrices, we have to take the next step. We have to multiply the matrix wih the input vector. Btw. this is exactly what we have manually done in our previous example.",
            "$$ ⎛⎝⎜⎜⎜y1y2y3y4⎞⎠⎟⎟⎟=⎛⎝⎜⎜⎜w11w21w31w41w12w22w32w42w13w23w33w43⎞⎠⎟⎟⎟⎛⎝⎜x1x2x3⎞⎠⎟=⎛⎝⎜⎜⎜w11⋅x1+w12⋅x2+w13⋅x3w21⋅x1+w22⋅x2+w23⋅x3w31⋅x1+w32⋅x2+w33⋅x3w41⋅x1+w42⋅x2+w43⋅x3⎞⎠⎟⎟⎟ $$",
            "We have a similar situation for the 'who' matrix between hidden and output layer. So the output z1 and z2 from the nodes o1 and o2 can also be calculated with matrix multiplications:",
            "$$ (z1z2)=(wh11wh21wh12wh22wh13wh23wh14wh24)⎛⎝⎜⎜⎜y1y2y3y4⎞⎠⎟⎟⎟=(wh11⋅y1+wh12⋅y2+wh13⋅y3+wh14⋅y4wh21⋅y1+wh22⋅y2+wh23⋅y3+wh24⋅y4) $$",
            "You might have noticed that something is missing in our previous calculations. We showed in our introductory chapter Neural Networks from Scratch in Python that we have to apply an activation or step function Φ on each of these sums.",
            "The following picture depicts the whole flow of calculation, i.e. the matrix multiplication and the succeeding multiplication. The matrix multiplication between the matrix wih and the matrix of the values of the input nodes x1,x2,x3 calculates the output which will be passed to the activation function.",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weights_input2hidden.png", "Weights Array from input to hidden layer with calculation"),
            "The final output y1,y2,y3,y4 is the input of the weight matrix who:",
            "Even though treatment is completely analogue, we will also have a detailled look at what is going on between our hidden layer and the output layer:",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weights_hidden2output.png", "Weights Array from hidden to output layer with calculation"),
        ])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class InitializingTheWeightMatrices(HierBlock):
    def __init__(self):
        super().__init__("Initializing the weight matrices", [
            "One of the important choices which have to be made before training a neural network consists in initializing the weight matrices. We don't know anything about the possible weight, when we start. So, we could start with arbitrary values?",
            "As we have seen the input to all the nodes except the input nodes is calculated by applying the activation function to the following sum:",
            "$$ yj=∑i=1nwji⋅xi $$",
            "(with n being the number of nodes in the previous layer and yj is the input to a node of the next layer)",
            "We can easily see that it would not be a good idea to set all the weight values to 0, because in this case the result of this summation will always be zero. This means that our network will be incapable of learning. This is the worst choice, but initializing a weight matrix to ones is also a bad choice.",
            "The values for the weight matrices should be chosen randomly and not arbitrarily. By choosing a random normal distribution we have broken possible symmetric situations, which are bad for the learning process.",
            "There are various ways to initialize the weight matrices randomly. The first one we will introduce is the unity function from numpy.random. It creates samples which are uniformly distributed over the half-open interval [low, high), which means that low is included and high is excluded. Each value within the given interval is equally likely to be drawn by 'uniform'.",
            cbk(None, """
import numpy as np
number_of_samples = 1200
low = -1
high = 0
s = np.random.uniform(low, high, number_of_samples)
# all values of s are within the half open interval [-1, 0) :
print(np.all(s >= -1) and np.all(s < 0))
            """, """
True
            """),
            "The histogram of the samples, created with the uniform function in our previous example, looks like this:",
            cbk(None, """
import matplotlib.pyplot as plt
plt.hist(s)
plt.show()
            """, None),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/initialization_0.png", None),
            "The next function we will look at is 'binomial' from numpy.binomial:",
            "`binomial(n, p, size=None)`",
            "It draws samples from a binomial distribution with specified parameters, n trials and p probability of success where n is an integer >= 0 and p is a float in the interval [0,1]. (n may be input as a float, but it is truncated to an integer in use)",
            cbk(None, """
s = np.random.binomial(100, 0.5, 1200)
plt.hist(s)
plt.show()
            """, None),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/initialization_1.png", None),
            "We like to create random numbers with a normal distribution, but the numbers have to be bounded. This is not the case with np.random.normal(), because it doesn't offer any bound parameter.",
            "We can use truncnorm from scipy.stats for this purpose.",
            "The standard form of this distribution is a standard normal truncated to the range [a, b] — notice that a and b are defined over the domain of the standard normal. To convert clip values for a specific mean and standard deviation, use:",
            "a, b = (myclip_a - my_mean) / my_std, (myclip_b - my_mean) / my_std",
            cbk(None, """
from scipy.stats import truncnorm
s = truncnorm(a=-2/3., b=2/3., scale=1, loc=0).rvs(size=1000)
plt.hist(s)
plt.show()
            """, None),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/initialization_2.png", None),
            "The function 'truncnorm' is difficult to use. To make life easier, we define a function 'truncated_normal' in the following to fascilitate this task:",
            cbk(None, """
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
X = truncated_normal(mean=0, sd=0.4, low=-0.5, upp=0.5)
s = X.rvs(10000)
plt.hist(s)
plt.show()
            """, None),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/initialization_3.png", None),
            "Further examples:",
            cbk(None, """
X1 = truncated_normal(mean=2, sd=1, low=1, upp=10)
X2 = truncated_normal(mean=5.5, sd=1, low=1, upp=10)
X3 = truncated_normal(mean=8, sd=1, low=1, upp=10)
import matplotlib.pyplot as plt
fig, ax = plt.subplots(3, sharex=True)
ax[0].hist(X1.rvs(10000), normed=True)
ax[1].hist(X2.rvs(10000), normed=True)
ax[2].hist(X3.rvs(10000), normed=True)
plt.show()
            """, None),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/initialization_4.png", None),
            "We will create the link weights matrix now. 'truncated_normal' is ideal for this purpose. It is a good idea to choose random values from within the interval",
            "$$ \\left( - \\frac{1}{\\sqrt{n}}, \\frac{1}{\\sqrt{n}} \\right) $$",
            "where n denotes the number of input nodes.",
            "So we can create our \"wih\" matrix with:",
            cbk(None, """
no_of_input_nodes = 3
no_of_hidden_nodes = 4
rad = 1 / np.sqrt(no_of_input_nodes)
X = truncated_normal(mean=2, sd=1, low=-rad, upp=rad)
wih = X.rvs((no_of_hidden_nodes, no_of_input_nodes))
wih
            """, None),
            "The previous code returned the following result:",
            cbk(None, """
array([[-0.356241  ,  0.46875865,  0.41897957],
       [ 0.43267439, -0.10009341,  0.35524547],
       [ 0.45234311,  0.39339294,  0.365379  ],
       [ 0.49457071, -0.44498887,  0.47409918]])
            """, None),
            "Similarly, we can now define the \"who\" weight matrix:",
            cbk(None, """
no_of_hidden_nodes = 4
no_of_output_nodes = 2
rad = 1 / np.sqrt(no_of_hidden_nodes)  # this is the input in this layer!
X = truncated_normal(mean=2, sd=1, low=-rad, upp=rad)
who = X.rvs((no_of_output_nodes, no_of_hidden_nodes))
who
            """, None),
            "After having executed the Python code above we received the following output:",
            cbk(None, """
array([[ 0.03743593,  0.34516431,  0.11852342, -0.10899819],
       [ 0.11039838,  0.41685055, -0.39363526,  0.07941089]])
            """, None),
        ])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ANeuralNetworkClass(HierBlock):
    def __init__(self):
        super().__init__("A Neural Network Class", [
            "We are ready now to start with the implementation of our neural network in Python. We will need to define the train and run method later. Instead of defining the weight matrices within the __init__ method of our Python class, we define them in a sparate method for reasons of clarity:",
            cbk(None, """
import numpy as np
class NeuralNetwork:
    
    def __init__(self, 
                 no_of_in_nodes, 
                 no_of_out_nodes, 
                 no_of_hidden_nodes,
                 learning_rate):
        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes 
        self.no_of_hidden_nodes = no_of_hidden_nodes
        self.learning_rate = learning_rate  
        self.create_weight_matrices()
        
    def create_weight_matrices(self):
        rad = 1 / np.sqrt(self.no_of_in_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes, 
                                       self.no_of_in_nodes))
        rad = 1 / np.sqrt(self.no_of_hidden_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes, 
                                        self.no_of_hidden_nodes))
             
    
    def train(self):
        pass
    
    def run(self):
        pass
    
    
if __name__ == "__main__":
    simple_network = NeuralNetwork(no_of_in_nodes = 3, 
                                   no_of_out_nodes = 2, 
                                   no_of_hidden_nodes = 4,
                                   learning_rate = 0.1)
    print(simple_network.weights_in_hidden)
    print(simple_network.weights_hidden_out)
            """, """
[[ 0.10607641 -0.05716482  0.55752363]
 [ 0.33701589  0.05461437  0.5521666 ]
 [ 0.11990863 -0.29320233 -0.43600856]
 [-0.18218775 -0.20794852 -0.39419628]]
[[  4.82634085e-04  -4.97611184e-01  -3.25708215e-01  -2.61086173e-01]
 [ -2.04995922e-01  -7.08439635e-02   2.66347839e-01   4.87601670e-01]]
            """),
        ])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ActivationFunctionsSigmoidAndReLU(HierBlock):
    def __init__(self):
        super().__init__("Activation Functions, Sigmoid and ReLU", [
            "Running our neural network on some input means that we will have a matrix multiplications of the weight vectors and the inputs. We have to apply an activation function on the output values. There are lots of different activation functions used in neural networks. The sigmoid function belongs to the most often used activation functions.",
            "It is defined as",
            "$$ \\sigma(x) = \\frac{1}{1 + e^{-x}} $$",
            "Let us have a look at the graph of the sigmoid function. We use matplotlib to plot the sigmoid function:",
            cbk(None, """
import numpy as np
import matplotlib.pyplot as plt
def sigma(x):
    return 1 / (1 + np.exp(-x))
X = np.linspace(-5, 5, 100)
plt.plot(X, sigma(X),'b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Sigmoid Function')
plt.grid()
plt.text(4, 0.8, r'$\sigma(x)=\frac{1}{1+e^{-x}}$', fontsize=16)
plt.show()
            """, None),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/sigmoid.png", None),
            "Instead of defining the sigmoid function ourselves, we can use the expit function from scipy.special, which is an implementation of the sigmoid function. It can be applied on various data classes like int, float, list, numpy,ndarray and so on. The result is an ndarray of the same shape as the input data x.",
            cbk(None, """
from scipy.special import expit
print(expit(3.4))
print(expit([3, 4, 1]))
print(expit(np.array([0.8, 2.3, 8])))
            """, """
0.967704535302
[ 0.95257413  0.98201379  0.73105858]
[ 0.68997448  0.90887704  0.99966465]
            """),
        ])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AddingARunMethod(HierBlock):
    def __init__(self):
        super().__init__("Adding a run Method", [
            "We can use this as the activation function of our neural network. As you most probably know, we can directly assign a new name, when we import the function:",
            cbk(None, """
from scipy.special import expit as activation_function
import numpy as np
from scipy.special import expit as activation_function
from scipy.stats import truncnorm
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
class NeuralNetwork:
           
    def __init__(self, 
                 no_of_in_nodes, 
                 no_of_out_nodes, 
                 no_of_hidden_nodes,
                 learning_rate):
        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes
        self.no_of_hidden_nodes = no_of_hidden_nodes
        self.learning_rate = learning_rate 
        self.create_weight_matrices()
        
    def create_weight_matrices(self):
        \"\"\" A method to initialize the weight matrices of the neural network\"\"\"
        rad = 1 / np.sqrt(self.no_of_in_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes, 
                                       self.no_of_in_nodes))
        rad = 1 / np.sqrt(self.no_of_hidden_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes, 
                                        self.no_of_hidden_nodes))
    
    
    def train(self, input_vector, target_vector):
        pass
            
    
    def run(self, input_vector):
        \"\"\"
        running the network with an input vector input_vector. 
        input_vector can be tuple, list or ndarray
        \"\"\"
        
        # turning the input vector into a column vector
        input_vector = np.array(input_vector, ndmin=2).T
        output_vector = np.dot(self.weights_in_hidden, input_vector)
        output_vector = activation_function(output_vector)
        
        output_vector = np.dot(self.weights_hidden_out, output_vector)
        output_vector = activation_function(output_vector)
    
        return output_vector
        """, None),
            "There is still a train method missing. We can instantiate and run this network, but the results will not make sense. They are based on the random weight matrices:",
            cbk(None, """
simple_network = NeuralNetwork(no_of_in_nodes=2, 
                               no_of_out_nodes=2, 
                               no_of_hidden_nodes=10,
                               learning_rate=0.6)
simple_network.run([(3, 4)])
            """, None),
            "The previous code returned the following:",
            cbk(None, """
array([[ 0.66413143],
       [ 0.45385657]])
            """, None),
            "We can also define our own sigmoid function with the decorator vectorize from numpy:",
            cbk(None, """
@np.vectorize
def sigmoid(x):
    return 1 / (1 + np.e ** -x)
#sigmoid = np.vectorize(sigmoid)
sigmoid([3, 4, 5])
            """, None),
            "The above code returned the following result:",
            cbk(None, """
array([ 0.95257413,  0.98201379,  0.99330715])
            """, None),
            "We add training support in our next class definition, i.e. we define the method 'train':",
            cbk(None, """
import numpy as np
@np.vectorize
def sigmoid(x):
    return 1 / (1 + np.e ** -x)
activation_function = sigmoid
from scipy.stats import truncnorm
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
class NeuralNetwork:
    
    def __init__(self, 
                 no_of_in_nodes, 
                 no_of_out_nodes, 
                 no_of_hidden_nodes,
                 learning_rate):
        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes
        self.no_of_hidden_nodes = no_of_hidden_nodes
        self.learning_rate = learning_rate 
        self.create_weight_matrices()
        
    def create_weight_matrices(self):
        \"\"\" A method to initialize the weight matrices of the neural network\"\"\"
        rad = 1 / np.sqrt(self.no_of_in_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes, 
                                       self.no_of_in_nodes))
        rad = 1 / np.sqrt(self.no_of_hidden_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes, 
                                        self.no_of_hidden_nodes))
        
    
    def train(self, input_vector, target_vector):
        # input_vector and target_vector can be tuple, list or ndarray
        
        input_vector = np.array(input_vector, ndmin=2).T
        target_vector = np.array(target_vector, ndmin=2).T
        
        output_vector1 = np.dot(stelf.weights_in_hidden, input_vector)
        output_vector_hidden = activation_function(output_vector1)
        
        output_vector2 = np.dot(self.weights_hidden_out, output_vector_hidden)
        output_vector_network = activation_function(output_vector2)
        
        output_errors = target_vector - output_vector_network
        # update the weights:
        tmp = output_errors * output_vector_network * (1.0 - output_vector_network)     
        tmp = self.learning_rate  * np.dot(tmp, output_vector_hidden.T)
        self.weights_hidden_out += tmp
        # calculate hidden errors:
        hidden_errors = np.dot(self.weights_hidden_out.T, output_errors)
        # update the weights:
        tmp = hidden_errors * output_vector_hidden * (1.0 - output_vector_hidden)
        self.weights_in_hidden += self.learning_rate * np.dot(tmp, input_vector.T)
           
    
    def run(self, input_vector):
        # input_vector can be tuple, list or ndarray
        input_vector = np.array(input_vector, ndmin=2).T
        output_vector = np.dot(self.weights_in_hidden, input_vector)
        output_vector = activation_function(output_vector)
        
        output_vector = np.dot(self.weights_hidden_out, output_vector)
        output_vector = activation_function(output_vector)
    
        return output_vector
        """, None),
            "We will test our network with the same example, we created in the chapter [Neural Networks from Scratch] (neural_networks.php):",
            cbk(None, """
import numpy as np
from matplotlib import pyplot as plt
data1 = [((3, 4), (0.99, 0.01)), ((4.2, 5.3), (0.99, 0.01)), 
         ((4, 3), (0.99, 0.01)), ((6, 5), (0.99, 0.01)), 
         ((4, 6), (0.99, 0.01)), ((3.7, 5.8), (0.99, 0.01)), 
         ((3.2, 4.6), (0.99, 0.01)), ((5.2, 5.9), (0.99, 0.01)), 
         ((5, 4), (0.99, 0.01)), ((7, 4), (0.99, 0.01)), 
         ((3, 7), (0.99, 0.01)), ((4.3, 4.3), (0.99, 0.01))]
data2 = [((-3, -4), (0.01, 0.99)), ((-2, -3.5), (0.01, 0.99)), 
         ((-1, -6), (0.01, 0.99)), ((-3, -4.3), (0.01, 0.99)), 
         ((-4, -5.6), (0.01, 0.99)), ((-3.2, -4.8), (0.01, 0.99)), 
         ((-2.3, -4.3), (0.01, 0.99)), ((-2.7, -2.6), (0.01, 0.99)), 
         ((-1.5, -3.6), (0.01, 0.99)), ((-3.6, -5.6), (0.01, 0.99)), 
         ((-4.5, -4.6), (0.01, 0.99)), ((-3.7, -5.8), (0.01, 0.99))]
data = data1 + data2
np.random.shuffle(data)
points1, labels1 = zip(*data1)
X, Y = zip(*points1)
plt.scatter(X, Y, c="r")
points2, labels2 = zip(*data2)
X, Y = zip(*points2)
plt.scatter(X, Y, c="b")
plt.show()
            """, None),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/run_method_0.png", None),
            cbk(None, """
simple_network = NeuralNetwork(no_of_in_nodes=2, 
                               no_of_out_nodes=2, 
                               no_of_hidden_nodes=2,
                               learning_rate=0.6)
    
size_of_learn_sample = int(len(data)*0.9)
learn_data = data[:size_of_learn_sample]
test_data = data[-size_of_learn_sample:]
print()
for i in range(size_of_learn_sample):
    point, label = learn_data[i][0], learn_data[i][1]
    simple_network.train(point, label)
    
for i in range(size_of_learn_sample):
    point, label = learn_data[i][0], learn_data[i][1]
    cls1, cls2 =simple_network.run(point)
    print(point, cls1, cls2, end=": ")
    if cls1 > cls2:
        if label == (0.99, 0.01):
            print("class1 correct", label)
        else:
            print("class2 incorrect", label)
    else:
        if label == (0.01, 0.99):
            print("class1 correct", label)
        else:
            print("class2 incorrect", label)
            """, None),
            cbk(None, """
(4.2, 5.3) [ 0.69567493] [ 0.36574485]: class1 correct (0.99, 0.01)
(4, 6) [ 0.69599417] [ 0.3655189]: class1 correct (0.99, 0.01)
(4.3, 4.3) [ 0.69465373] [ 0.36646922]: class1 correct (0.99, 0.01)
(3.2, 4.6) [ 0.69434421] [ 0.36667755]: class1 correct (0.99, 0.01)
(3, 7) [ 0.69614915] [ 0.36540844]: class1 correct (0.99, 0.01)
(4, 3) [ 0.69015391] [ 0.36965891]: class1 correct (0.99, 0.01)
(5.2, 5.9) [ 0.69614659] [ 0.36541353]: class1 correct (0.99, 0.01)
(-2.3, -4.3) [ 0.2887322] [ 0.63701291]: class1 correct (0.01, 0.99)
(-3.6, -5.6) [ 0.28571677] [ 0.63918581]: class1 correct (0.01, 0.99)
(3, 4) [ 0.69265701] [ 0.36786409]: class1 correct (0.99, 0.01)
(6, 5) [ 0.69593054] [ 0.365569]: class1 correct (0.99, 0.01)
(-1.5, -3.6) [ 0.29421745] [ 0.6330841]: class1 correct (0.01, 0.99)
(-3.7, -5.8) [ 0.2855751] [ 0.63928833]: class1 correct (0.01, 0.99)
(-2, -3.5) [ 0.29319957] [ 0.63379548]: class1 correct (0.01, 0.99)
(3.7, 5.8) [ 0.69583411] [ 0.36563081]: class1 correct (0.99, 0.01)
(5, 4) [ 0.69461572] [ 0.36650241]: class1 correct (0.99, 0.01)
(-2.7, -2.6) [ 0.29847545] [ 0.62995199]: class1 correct (0.01, 0.99)
(7, 4) [ 0.69548262] [ 0.36589335]: class1 correct (0.99, 0.01)
(-3.2, -4.8) [ 0.2866943] [ 0.63847813]: class1 correct (0.01, 0.99)
(-3, -4.3) [ 0.28781573] [ 0.63766572]: class1 correct (0.01, 0.99)
(-3, -4) [ 0.28863857] [ 0.63706791]: class1 correct (0.01, 0.99)
            """, None),
            "Something to be done in a future release: We will define at a later point also different activation functions like the ReLU:",
            cbk(None, """
# alternative activation function
def ReLU(x):
    return np.maximum(0.0, x)
# derivation of relu
def ReLU_derivation(x):
    if x <= 0:
        return 0
    else:
        return 1
            """, None),
            cbk(None, """
import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-5, 5, 100)
plt.plot(X, ReLU(X),'b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('ReLU Function')
plt.grid()
plt.text(3, 0.8, r'$ReLU(x)=max(0.0, x)$', fontsize=16)
plt.show()
            """, None),
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/run_method_1.png", None),
        ])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NeuralNetworkWithBiasNodes(HierBlock):
    def __init__(self):
        super().__init__("Neural Network with Bias Nodes", [
            "A bias node is a node that is always returning the same output. In other words: It is a node which is not depending on some input and it does not have any input. The value of a bias node is often set to one, but it can be other values as well. Except 0 which doesn't make sense. If a neural network does not have a bias node in a given layer, it will not be able to produce output in the next layer that differs from 0 when the feature values are 0. Generally speaking, we can say that bias nodes are used to increase the flexibility of the network to fit the data. Usually, there will be not more than one bias node per layer. The only exception is the output layer, because it makes no sense to add a bias node to this layer.",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weights_input2hidden_bias.png", "Weights Array from input to hidden layer with bias"),
            "We can see from this diagram that our weight matrix will have one more column and the bias value is added to the input vector:",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weight_input_matrix_multiplication_bias.png", "Weights Array from hidden to output layer with bias, matrix multiplication"),
            "Again, the situation for the weight matrix between the hidden and the outputlayer is similar:",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weights_hidden2output_bias.png", "Weights Array from hidden to output layer with bias"),
            "The same is true for the corresponding matrix:",
            ibk("/home/lcmcafee/Dropbox/Code/nimra/src/python/nimra/modules/nodes/web/python-course.eu/neural_networks_with_python_numpy/orig_files/weight_hidden_matrix_multiplication_bias.png", "Weights Array from hidden to output layer with bias, matrix multiplication"),
            "The following is a complete Python class implementing our network with bias nodes:",
            cbk(None, """
import numpy as np
@np.vectorize
def sigmoid(x):
    return 1 / (1 + np.e ** -x)
activation_function = sigmoid
from scipy.stats import truncnorm
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
class NeuralNetwork:
        
    
    def __init__(self, 
                 no_of_in_nodes, 
                 no_of_out_nodes, 
                 no_of_hidden_nodes,
                 learning_rate,
                 bias=None
                ):  
        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes
        
        self.no_of_hidden_nodes = no_of_hidden_nodes
            
        self.learning_rate = learning_rate 
        self.bias = bias
        self.create_weight_matrices()
    
        
    
    def create_weight_matrices(self):
        \"\"\" A method to initialize the weight matrices of the neural 
        network with optional bias nodes\"\"\"
        
        bias_node = 1 if self.bias else 0
        
        rad = 1 / np.sqrt(self.no_of_in_nodes + bias_node)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes, 
                                       self.no_of_in_nodes + bias_node))
        rad = 1 / np.sqrt(self.no_of_hidden_nodes + bias_node)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes, 
                                        self.no_of_hidden_nodes + bias_node))
        
        
        
    def train(self, input_vector, target_vector):
        # input_vector and target_vector can be tuple, list or ndarray
        
        bias_node = 1 if self.bias else 0
        if self.bias:
            # adding bias node to the end of the inpuy_vector
            input_vector = np.concatenate( (input_vector, [self.bias]) )
                                    
            
        input_vector = np.array(input_vector, ndmin=2).T
        target_vector = np.array(target_vector, ndmin=2).T
        
        output_vector1 = np.dot(self.weights_in_hidden, input_vector)
        output_vector_hidden = activation_function(output_vector1)
        
        if self.bias:
            output_vector_hidden = np.concatenate( (output_vector_hidden, [[self.bias]]) )
        
        
        output_vector2 = np.dot(self.weights_hidden_out, output_vector_hidden)
        output_vector_network = activation_function(output_vector2)
        
        output_errors = target_vector - output_vector_network
        # update the weights:
        tmp = output_errors * output_vector_network * (1.0 - output_vector_network)     
        tmp = self.learning_rate  * np.dot(tmp, output_vector_hidden.T)
        self.weights_hidden_out += tmp
        # calculate hidden errors:
        hidden_errors = np.dot(self.weights_hidden_out.T, output_errors)
        # update the weights:
        tmp = hidden_errors * output_vector_hidden * (1.0 - output_vector_hidden)
        if self.bias:
            x = np.dot(tmp, input_vector.T)[:-1,:]     # ???? last element cut off, ???
        else:
            x = np.dot(tmp, input_vector.T)
        self.weights_in_hidden += self.learning_rate * x
        
       
    
    def run(self, input_vector):
        # input_vector can be tuple, list or ndarray
        
        if self.bias:
            # adding bias node to the end of the inpuy_vector
            input_vector = np.concatenate( (input_vector, [1]) )
        input_vector = np.array(input_vector, ndmin=2).T
        output_vector = np.dot(self.weights_in_hidden, input_vector)
        output_vector = activation_function(output_vector)
        
        if self.bias:
            output_vector = np.concatenate( (output_vector, [[1]]) )
            
        output_vector = np.dot(self.weights_hidden_out, output_vector)
        output_vector = activation_function(output_vector)
    
        return output_vector
            """, None),
            cbk(None, """
class1 = [(3, 4), (4.2, 5.3), (4, 3), (6, 5), (4, 6), (3.7, 5.8),
          (3.2, 4.6), (5.2, 5.9), (5, 4), (7, 4), (3, 7), (4.3, 4.3) ] 
class2 = [(-3, -4), (-2, -3.5), (-1, -6), (-3, -4.3), (-4, -5.6), 
          (-3.2, -4.8), (-2.3, -4.3), (-2.7, -2.6), (-1.5, -3.6), 
          (-3.6, -5.6), (-4.5, -4.6), (-3.7, -5.8) ]
labeled_data = []
for el in class1:
    labeled_data.append( [el, [1, 0]])
for el in class2:
    labeled_data.append([el, [0, 1]])
  
np.random.shuffle(labeled_data)
print(labeled_data[:10])
data, labels = zip(*labeled_data)
labels = np.array(labels)
data = np.array(data)
            """, """
[[(-1, -6), [0, 1]], [(-2.3, -4.3), [0, 1]], [(-3, -4), [0, 1]], [(-2, -3.5), [0, 1]], [(3.2, 4.6), [1, 0]], [(-3.7, -5.8), [0, 1]], [(4, 3), [1, 0]], [(4, 6), [1, 0]], [(3.7, 5.8), [1, 0]], [(5.2, 5.9), [1, 0]]]
            """),
            cbk(None, """
simple_network = NeuralNetwork(no_of_in_nodes=2, 
                               no_of_out_nodes=2, 
                               no_of_hidden_nodes=10,
                               learning_rate=0.1,
                               bias=None)
    
for _ in range(20):
    for i in range(len(data)):
        simple_network.train(data[i], labels[i])
for i in range(len(data)):
    print(labels[i])
    print(simple_network.run(data[i]))
            """, """
[0 1]
[[ 0.06857234]
 [ 0.93333256]]
[0 1]
[[ 0.0694426 ]
 [ 0.93263667]]
[0 1]
[[ 0.06890567]
 [ 0.93314354]]
[0 1]
[[ 0.07398586]
 [ 0.92826171]]
[1 0]
[[ 0.91353761]
 [ 0.08620027]]
[0 1]
[[ 0.06598966]
 [ 0.93595685]]
[1 0]
[[ 0.90963169]
 [ 0.09022392]]
[1 0]
[[ 0.9155282 ]
 [ 0.08423438]]
[1 0]
[[ 0.91531178]
 [ 0.08444738]]
[1 0]
[[ 0.91575254]
 [ 0.08401871]]
[1 0]
[[ 0.91164767]
 [ 0.08807266]]
[0 1]
[[ 0.06818507]
 [ 0.93384242]]
[0 1]
[[ 0.07609557]
 [ 0.92620649]]
[0 1]
[[ 0.06651258]
 [ 0.93543384]]
[1 0]
[[ 0.91411049]
 [ 0.08570024]]
[1 0]
[[ 0.91409934]
 [ 0.08567811]]
[0 1]
[[ 0.06711438]
 [ 0.93487441]]
[1 0]
[[ 0.91517701]
 [ 0.08458689]]
[1 0]
[[ 0.91550873]
 [ 0.08427926]]
[1 0]
[[ 0.91562321]
 [ 0.08414424]]
[0 1]
[[ 0.06613625]
 [ 0.93581576]]
[0 1]
[[ 0.0659944]
 [ 0.9359505]]
[0 1]
[[ 0.07744433]
 [ 0.92481335]]
[1 0]
[[ 0.91498511]
 [ 0.08485322]]
In [ ]:
            """),
        ])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Index(WebNode):
    def __init__(self):
        super().__init__(
            "How to build your own Neural Network from scratch in Python",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(Introduction())
        self.add(ASimpleArtificialNeuralNetworkStructure())
        self.add(WeightsAndMatrices())
        self.add(InitializingTheWeightMatrices())
        self.add(ANeuralNetworkClass())
        self.add(ActivationFunctionsSigmoidAndReLU())
        self.add(AddingARunMethod())
        self.add(NeuralNetworkWithBiasNodes())

# eof
