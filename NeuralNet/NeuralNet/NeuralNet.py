import numpy as np
import math
from scipy.special import expit


class NeuralNet:
    """
    Class to simulate an Artificial Neural Network.
    """

    def __init__(self, n_input, n_hidden, n_output):
        """
        Constructor for the Neural Network class.

        :param n_input: the number of input units.
        :param n_hidden: the number of hidden units.
        :param n_output: the number of output units.
        :return: nothing
        """

        # for the calculation of accuracy
        self.counter = 0

        self.learn_rate = np.float64(.05)

        self.n_input = n_input
        self.n_hidden = n_hidden
        self.n_output = n_output

        # all the numpy arrays used throughout the class. Initialized for 
        # memory purposes.
        self.temp_hidden0 = np.zeros(n_hidden)
        self.temp_hidden = np.zeros(n_hidden)
        self.temp_out0 = np.zeros(n_output)
        self.temp_out = np.zeros(n_output)
        self.hidden_out = np.zeros(n_hidden)
        self.final_out = np.zeros(n_output)
        self.actual = np.zeros(n_output)
        self.final_output_err = np.zeros(n_output)
        self.final_hidden_err = np.zeros(n_hidden)
        self.delta_weights = np.zeros(n_input*n_hidden)
        self.bias_delta_weights = np.zeros(n_hidden)
        self.output_delta_weights = np.zeros(n_output)
        self.outbias_delta_weights = np.zeros(n_output)

        # matrix weights between the input and hidden layer
        self.h_weights = np.random.uniform(-1.0, 1.0, size=(self.n_input+1, self.n_hidden))

        # matrix of weight between the hidden and output layer
        self.o_weights = np.random.uniform(-1.0, 1.0, size=(self.n_hidden+1, self.n_output))

        self.output_ones = np.ones(self.actual.size)
        self.hidden_ones = np.ones(len(self.o_weights)-1)

    # simulates forward propagation through the neural net
    def for_prop(self, data):
        """
        Simulates forward propagation through the Neural Net.

        :param data: the image array to be propagated.
        :return: the output from the output and hidden layers.
        """

        # append a -1 for the bias
        d = np.append(data, [-1])

        # send the input through the hidden layer and apply the sigmoid
        self.temp_hidden0 = self.h_weights*d[:, np.newaxis]
        np.sum(self.temp_hidden0, axis=0, out=self.temp_hidden)
        self.hidden_out = expit(self.temp_hidden)
        final_hidden_out = np.append(self.hidden_out, [-1])

        # same as before, multiply inputs by weights
        # sum them together and pass them through a sigmoid
        self.temp_out0 = self.o_weights*final_hidden_out[:, np.newaxis]
        np.sum(self.temp_out0, axis=0, out=self.temp_out)
        self.final_out = expit(self.temp_out)

        return self.final_out, self.hidden_out

    def back_prop(self, data, target):
        """
        Simulates backpropagation through the Neural Net.

        :param data: The image array to be propagated.
        :param target: the correct classification for the data
        :return: the output from for_prop()
        """
        # the output and hidden layer outputs
        prop0, prop1 = self.for_prop(data)

        # create the target values dependent on what the classifier was.
        self.actual[target] = 1

        # here is the actual error calculation for the output layers.
        # finalErr is an array of all the output nodes' error terms.
        output_err_0 = self.actual - prop0
        output_err_1 = self.output_ones - prop0

        self.final_output_err = prop0*output_err_1*output_err_0

        # hidden units
        hidden_err_0 = self.hidden_ones-prop1

        hidden_err_1 = self.o_weights*self.final_output_err[np.newaxis, :]
        hidden_err_1 = np.sum(hidden_err_1, axis=1)

        hidden_err_1 = np.delete(hidden_err_1, hidden_err_1.size-1)

        # here is the error calculation for the hidden layer.
        self.final_hidden_err = prop1*hidden_err_0*hidden_err_1

        self.delta_weights = self.final_hidden_err*data[:, np.newaxis]
        self.delta_weights *= self.learn_rate

        # finally, update the weights.
        nuhidden_weights = np.add(self.h_weights[:self.n_input], self.delta_weights)

        self.bias_delta_weights = self.final_hidden_err*-1
        self.bias_delta_weights *= self.learn_rate
        nuhidden_bias = np.add(self.h_weights[self.n_input:], self.bias_delta_weights)

        self.h_weights = np.concatenate((nuhidden_weights, nuhidden_bias), axis=0)

        self.output_delta_weights = self.final_output_err*prop1[:, np.newaxis]
        self.output_delta_weights *= self.learn_rate
        nuoutput_weights = np.add(self.o_weights[:self.n_hidden], self.output_delta_weights)

        self.outbias_delta_weights = self.final_output_err*-1
        self.outbias_delta_weights *= self.learn_rate

        nuoutput_bias = np.add(self.o_weights[self.n_hidden:], self.outbias_delta_weights)

        self.o_weights = np.concatenate((nuoutput_weights, nuoutput_bias), axis=0)

        self.actual[target] = 0
        return prop0

    def update_learn_rate(self):
        """
        Used as momentum to slow down the learning rate after a while.

        :return: nothing
        """
        self.learn_rate *= np.float64(.9999)

    def print_for(self):
        """
        Used for testing purposes. Printing certain variables to check the values.

        :return: nothing
        """
        print "The hidden units after the first pass and sigmoid function (with threshold input)", self.final_hidden_out
        print "Here is the final output", self.final_out