import numpy as np
import NeuralNet
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.metrics import confusion_matrix


def load_data(file_name):
    """
    Loads dataset from .csv file. Returns the dataset.

    :param file_name: name of the file to be read
    """

    data = np.genfromtxt(file_name, delimiter=",")
    return data


def main():
    # Used to plot the accuracies on the graph.
    plt.figure(1)
    train_plot0 = [0]
    test_plot0 = [0]
    train_plot1 = [0]
    test_plot1 = [0]
    train_plot2 = [0]
    test_plot2 = [0]

    train_actual_set = []
    train_guessed_set = []

    test_actual_set = []
    test_guessed_set = []


    d = load_data('train_partial.csv')
    print "done loading data"

    # Splitting the data and reassembling it.
    one, two, three = np.split(d, 3)

    data_sets = np.array([[np.concatenate((one,two), axis=0), three], [np.concatenate((one,three), axis=0), two],
                          [np.concatenate((three,two), axis=0), one]])

    epochs = 2400
    data = d[0]
    data = np.delete(data, [0])

    # Initialize Neural Net.
    n = NeuralNet.NeuralNet(data.size, data.size, 10)
    print "neural net created"

    # Begin training and testing the first dataset.
    for x in xrange(epochs):
        print "epoch", x
        counter = 0.0
        # Training
        for y in data_sets[0][0]:

            target = int(y[0])
            y = np.delete(y, [0])

            out = n.back_prop(y, target)
            if target == np.argmax(out):
                counter += 1.0
            if x == epochs-1:
                train_actual_set.append(target)
                train_guessed_set.append(np.argmax(out))
        # Testing
        counter1 = 0.0
        for z in data_sets[0][1]:
            target = int(z[0])
            z = np.delete(z, [0])
            out0, out1 = n.for_prop(z)
            if target == np.argmax(out0):
                counter1 += 1.0
            if x == epochs-1:
                test_actual_set.append(target)
                test_guessed_set.append(np.argmax(out0))
        train_accuracy = counter/data_sets[0][0].shape[0]
        test_accuracy = counter1/data_sets[0][1].shape[0]
        train_plot0.append(train_accuracy)
        test_plot0.append(test_accuracy)

    n = NeuralNet.NeuralNet(data.size, data.size, 10)
    for x in xrange(epochs):
        print "epoch", x
        counter = 0.0
        # Training
        for y in data_sets[1][0]:

            target = int(y[0])
            y = np.delete(y, [0])

            out = n.back_prop(y, target)
            if target == np.argmax(out):
                counter += 1.0
            if x == epochs-1:
                train_actual_set.append(target)
                train_guessed_set.append(np.argmax(out))
        # Testing
        counter1 = 0.0
        for z in data_sets[1][1]:
            target = int(z[0])
            z = np.delete(z, [0])
            out0, out1 = n.for_prop(z)
            if target == np.argmax(out0):
                counter1 += 1.0
            if x == epochs-1:
                test_actual_set.append(target)
                test_guessed_set.append(np.argmax(out0))
        train_accuracy = counter/data_sets[1][0].shape[0]
        test_accuracy = counter1/data_sets[1][1].shape[0]
        train_plot1.append(train_accuracy)
        test_plot1.append(test_accuracy)

    n = NeuralNet.NeuralNet(data.size, data.size, 10)
    for x in xrange(epochs):
        print "epoch", x
        counter = 0.0
        # Training
        for y in data_sets[2][0]:
            target = int(y[0])
            y = np.delete(y, [0])
            out = n.back_prop(y, target)
            if target == np.argmax(out):
                counter += 1.0
            if x == epochs-1:
                train_actual_set.append(target)
                train_guessed_set.append(np.argmax(out))
        # Testing
        counter1 = 0.0
        for z in data_sets[2][1]:
            target = int(z[0])
            z = np.delete(z, [0])
            out0, out1 = n.for_prop(z)
            if target == np.argmax(out0):
                counter1 += 1.0
            if x == epochs-1:
                test_actual_set.append(target)
                test_guessed_set.append(np.argmax(out0))
        train_accuracy = counter/data_sets[2][0].shape[0]
        test_accuracy = counter1/data_sets[2][1].shape[0]
        train_plot2.append(train_accuracy)
        test_plot2.append(test_accuracy)

    # Creation of the confusion matrices.
    train_conf = confusion_matrix(train_actual_set, train_guessed_set)
    test_conf = confusion_matrix(test_actual_set, test_guessed_set)
    print "training set confusion matrix", train_conf
    print "testing set confusion matrix", test_conf

    graph(train_plot0, test_plot0, train_plot1, test_plot1, train_plot2, test_plot2)


def graph(train_plot0, test_plot0, train_plot1, test_plot1, train_plot2, test_plot2):
    """
    Plots the accuracies of the training and testing sets of each dataset on a graph.

    :param train_plot0: array containing the accuracies of the first dataset's training runs.
    :param test_plot0: array containing the accuracies of the first dataset's testing runs.
    :param train_plot1: array containing the accuracies of the second dataset's training runs.
    :param test_plot1: array containing the accuracies of the second dataset's testing runs.
    :param train_plot2: array containing the accuracies of the third dataset's training runs.
    :param test_plot2: array containing the accuracies of the third dataset's testing runs.
    """

    plt.subplot(211)
    plt.plot(train_plot0, 'r-')
    plt.plot(train_plot1, 'g-')
    plt.plot(train_plot2, 'b-')
    plt.axis('tight')

    plt.subplot(212)
    plt.plot(test_plot0, 'r-')
    plt.plot(test_plot1, 'g-')
    plt.plot(test_plot2, 'b-')
    plt.axis('tight')
    plt.show()


if __name__ == "__main__":
    main()