"""
Project Euler Problem 6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10@ = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import cProfile
import time
import math

def main(number_count):
    sum_of_squares = 0
    square_of_sum = 0
    difference = 0

    for number in range(1, number_count+1):
        sum_of_squares += math.pow(number, 2)
        square_of_sum += number

    return sum_of_squares, math.pow(square_of_sum, 2), math.pow(square_of_sum, 2) - sum_of_squares


if __name__ == '__main__':

    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))

    cProfile.run('sum_of_squares, square_of_sum, difference = main(100)')
    print("sum of squares is: ", sum_of_squares, " square_of_sum: ", square_of_sum, " difference: ", difference)

    # print(list)

    print("--- %s seconds ---" % (time.time() - start_time))

