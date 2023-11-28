# CPSC 335 Fall 2023 Project 2
## Abstract
In this project: design, implement and analyze an exhaustive search algorithm, dynamic programming algorithm for solving the same problem.
## The Stock Purchase Maximization Problem
The problem seeks to maximize the number of stocks an investor may purchase, given a limited amount of available financial resources. The future values of these stocks are not considered at the time of purchase.

This problem can be mathematically represented as:

`input:` a set of items (<i>s<sub>i</sub></i>, <i>v<sub>i</sub></i>) each having a number of stocks <i>s<sub>i</sub></i> and value. <i>M</i> is the total available investment sum. 

`output:` maximum number of stocks, such that the total value of those stocks is at most <i>M</i>.

## Instructions
1. Have Python 3.11.5 installed.
2. Put in test cases in `input.txt`, where the first line is the stocks, and the second line is the total investment, each separated by a new line.
3. Run `py .\main.py` (or `python .\main.py` depending on how PATH is setup) in terminal.

## Exhaustive Approach
The exhaustive approach defines a recursive function `maximize` that explores all possible candidates of stocks. It considers two options for each stock: including it and excluding it. The function returns the maximum number of stocks that can be purchased within the given investment.

Time complexity: O(2<sup>n</sup>)

## Dynamic Approach
The dynamic approach creates a 2D array `dp` where `dp[i][j]` represents the maximum number of stocks that can be purchased with an investment of `j` considering only the first `i` stocks. We fill in this array iteratively, considering both including and excluding each stock in the calculation. 

Time complexity: O(n)

## Conclusion
This dynamic programming approach has a time complexity of O(n), which is much more efficient than the exhaustive recursive approach (time complexity: O(2<sup>n</sup>)) for larger inputs. This makes the dynamic approach significantly better than the exhaustive.

## Author
Ronald Lee (ronaldvlee@csu.fullerton.edu)