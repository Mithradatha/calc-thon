"""
Problem:
{
    Compute binomial coefficients for a given n and k.
}
Description:
{
    Binomial coefficients = (n choose k),
    where [n] is the number of total elements in the set
    and [k] is the number of elements in each subset of [n]=> number of combinations (unordered [k]-subsets).
}
Algorithm:
{
    Given (n choose k),
    1. Initialize a vector of length (k + 1)
    2. Set vector[0] = 1
    3. Set j = 0
    4. While j < k, Repeat steps 5 - 6
    5. Set vector[j + 1] = (vector[j] * (n - j)) / (j + 1)
    6. Set j = j + 1
    7. Return vector[k] as number of combinations
}
Notes:
{
    (n choose k) can be represented using Pascal's triangle. Pascal's triangle can be represented using an n+1 by k+1, zero-indexed, lower-triangular matrix where each entry in column [0] is equal to 1. One property of Pascal's triangle is that each entry in any given row can be calculated by using the previous entry in the same row. Since matrix[i][0], where i is in range 0..n, is equal to 1, there is enough information to calculate the entries in each row of the triangle independently. Therefore, (n choose k) can be calculated by finding the entry at matrix[n][k].
}
References:
{
    http://mathworld.wolfram.com/BinomialCoefficient.html

    https://en.wikipedia.org/wiki/Binomial_coefficient

    http://www.csl.mtu.edu/cs4321/www/Lectures/Lecture%2015%20-%20Dynamic%20Programming%20Binomial%20Coefficients.htm

    https://stackoverflow.com/questions/15580291/how-to-efficiently-calculate-a-row-in-pascals-triangle
{
"""

from sys import argv


def combinations(n, k):
    """
    n choose k

    Args:
        n (int): number of elements in set.
        k (int): number of elements in each subset.

    Returns:
        combinations (float).
    """

    # only save the rightmost entry
    cache = 1
    for i in range(k):
        cache = (cache * (n - i)) / (i + 1)
    return cache


if __name__ == '__main__':
    # argv[0] = program name
    n_args = len(argv) - 1

    if n_args == 2:
        try:
            n = int(argv[1])
            k = int(argv[2])
            r = combinations(n, k)
            try:
                print("{0} choose {1} is equal to: {2}".format(n, k, int(r)))
            except OverflowError:
                print("{0} choose {1} is equal to: {2}".format(n, k, r))
        except ValueError:
            print("n: {0} and k: {1} must be integers".format(
                argv[1], argv[2]))
    elif n_args < 2:
        print("please supply arguments n and k")
    else:
        print("too many arguments")
