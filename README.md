# Neural-Network-XOR-Problem
Artificial neural networks; It is a method that gives successful results in solving many daily life problems such as classification, modeling and estimation. Prediction and classification problems can be solved with the back propagation algorithm, which is widely used in artificial neural networks. By changing the parameters such as the number of layers of the network, the number of neurons in the layers, the number of iterations, the learning rate, the momentum coefficient, the activation function, the normalization method, the initial weights, the network can be trained and the performance of the network can be measured by testing the trained network.

With the book called Perceptrons, published by Marvin Minsky and Seymour Papert in 1969, it was argued that single-layer and feed-forward artificial neural networks cannot be a logical solution to every problem. By citing the XOR problem as an example, a discussion was started that would shelve the studies of artificial neural networks for a long time. Finally, a solution to this problem was found by creating multi-layer artificial neural networks with both forward and feedback.

For this example , we’re going to use a neural network with two inputs, two hidden neurons, two output neurons. Additionally, the hidden and output neurons will include a bias. we will examine coding in python language (without a library) for the solution of the XOR problem.

Artificial neural networks are computer systems developed with the aim of automatically performing abilities such as deriving new information, creating and discovering new information through learning, which is a feature unique to the human brain, without any assistance. Artificial neural networks; Inspired by the human brain, it emerged as a result of the mathematical modeling of the learning process. Artificial neural networks consist of three main parts;

## Input Layer
It is the initial layer of inputs to the neural network from the outside world. In this layer, as many cells and inputs as the number of inputs are transmitted from anything to the special layer.

## Hidden Layers
Starting from the input layer, it is processed and transmitted to a layer. The number of hidden layers and the network-to-network range of numbers in the hidden layer. It is from the cells in the hidden layers, the number of inputs and outputs.

 ## Output Layer
Transitions from inputs from the hidden layer and from inputs to incoming ones in accordance with the inputs. It can be a big part of what can happen at the beach. Each output has one output. Its one cell is connected to the whole in the previous layer.
<p align="center">
  <img width="635" height="425" src="https://user-images.githubusercontent.com/75435070/169088431-28da0e7b-1b1b-4780-b13c-cff542e57c66.png">
</p>

## The Forward Pass
Let a training set be given. The operations that proceed from left to right in the artificial neural network with the specified parameters of the inputs in this training set are called. In other words, it is the process from entering the input into the artificial neural network model to making the prediction.
<p align="center">
  <img width="436" height="371" src="https://user-images.githubusercontent.com/75435070/169084229-666a1fe5-1c6d-443f-b6fa-d4398458d9d5.png">
</p>

   
## The Backwards Pass
It is the most common teaching algorithm used in many applications. It is the most preferred teaching algorithm because it is easy to understand and can be proved mathematically. This algorithm is called backpropagation because it tries to reduce errors backwards from output to input. With backpropagation, our goal is to update each of the weights in the network so that the actual output is closer to the target output, thus minimizing the error for each output neuron and the network as a whole.


## ERROR FUNCTION
The result obtained by subtracting the desired output with the output function we found is our error function.

## Performance Analysis
<p align="center">
  <img width="853" height="516" src="https://user-images.githubusercontent.com/75435070/169090965-9d094bca-7f4f-446e-9707-de86de617fd4.png">
</p>

<p align="center">
  <img width="853" height="516" src="https://user-images.githubusercontent.com/75435070/169091845-63dbd7e5-3944-4e5d-a49e-00e1ba9fc8a1.png">
</p>

## References
* https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
* https://birolemekli.medium.com/yapay-sinir-a%C4%9Flar%C4%B1n%C4%B1-e%C4%9Fiterek-xor-problemi-%C3%A7%C3%B6zme-3cce784ff031
* https://chelewy.medium.com/yapay-sinir-a%C4%9Flar%C4%B1-ve-xor-problemi-ve-python-dili-kullan%C4%B1larak-%C3%A7%C3%B6z%C3%BCm%C3%BCn-yap%C4%B1lmas%C4%B1-cb08c3c6ef99
* https://en.wikipedia.org/wiki/Perceptrons_(book)
