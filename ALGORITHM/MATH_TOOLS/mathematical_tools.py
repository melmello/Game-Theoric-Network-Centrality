""" Mathematical module

    Module used purely as a mathematical library.

    No class are needed.

"""


def fast_binomial(first_newton_parameter, second_newton_parameter):
    """ Newton Binomial Coefficient calculation

        A fast way to calculate Newton Binomial Coefficients by Andrew Dalke.

        Args:
            first_newton_parameter (int): first parameter of the Newton Binomial Coefficient.
            second_newton_parameter (int): second parameter of the Newton Binomial Coefficient.

        Returns:
            n_took // k_took (int): the result of the Newton Binomial Coefficient

    """
    if 0 <= second_newton_parameter <= first_newton_parameter:
        n_tok = 1
        k_tok = 1
        for t in range(1, min(second_newton_parameter,
                              first_newton_parameter - second_newton_parameter) + 1):
            n_tok *= first_newton_parameter
            k_tok *= t
            first_newton_parameter -= 1
        return n_tok // k_tok
    else:
        return 0
