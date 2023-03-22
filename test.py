import objects.matrices.matrix as mat
import objects.matrices.matrixElement as matEl
import numpy as np
import random
import time
import matplotlib.pyplot as plt

from shor import shors_algorithm
from grover_sparse import grovers_algorithm

if __name__ == "__main__":

    option = 2

    if option == 1:
        # run Grover's algorithm
        list_of_times = []
        list_of_qubit_numbers = []
        for i in range(1, 11):
            n = random.randint(0, i)
            start_time = time.time()
            grovers_algorithm(i, n)
            time_it_took = time.time() - start_time
            list_of_times.append(time_it_took)
            list_of_qubit_numbers.append(i)

        print(list_of_times)
        # Create a figure and axis object
        fig, ax = plt.subplots()

        ax.plot(list_of_qubit_numbers, list_of_times, '-o')

        # Set the limits of the x and y axes
        ax.set_xlim([0, 10])
        ax.set_ylim([0, 100])

        # Set the labels for the x and y axes
        ax.set_xlabel('The number of qubits')
        ax.set_ylabel('Time of execution (in seconds)')
        ax.legend()
        # Set the title of the plot
        ax.set_title('Performance evaluation based on execution time')
        #fig.savefig('static/plot2.png')
        plt.show()


        # print(a, b)
        # print(time.time() - start_time)

    else:
        # run Shor's algorithm

        """nums = []
        for i in range(3):
            n = random.randint(0, 10000)
            while n % 2 == 0:
                n = random.randint(0, 10000)
            nums.append(n)

        print(nums)"""

        """list_of_times = []
                for item in rand_list:
                    start_time = time.time()
                    a, b = shors_algorithm(item)
                    time_it_took = time.time() - start_time
                    print("factors are ", a, b)
                    list_of_times.append(time_it_took)

                print(list_of_times)"""

        # these were precalculated
        rand_sorted_list = [51, 323, 865, 1011, 1689, 2285, 2863, 3387, 3729, 3941]
        times = [0.0330047607421875, 5.41510009765625, 7.18571925163269, 6.968134164810181, 55.93229818344116, 1244.950518131256, 1377.7137186527252, 152.76835465431213, 3.337860107421875e-06, 486.82393765449524]

        fig, ax = plt.subplots()

        ax.plot(rand_sorted_list, times, '-o')

        # Set the limits of the x and y axes
        ax.set_xlim([0, 4000])
        ax.set_ylim([0, 1500])

        # Set the labels for the x and y axes
        ax.set_xlabel('A number to factorise')
        ax.set_ylabel('Time of execution (in seconds)')
        # ax.legend()
        # Set the title of the plot
        ax.set_title('Performance evaluation based on execution time')
        # fig.savefig('static/plot2.png')
        plt.show()

        # factors = shors_algorithm(135)
        # print(factors)
