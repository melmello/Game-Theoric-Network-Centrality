""" Utility module

    Module used as a library of functions with an utility scope.

    No class are needed.

"""


def word_checker(user_input, possible_choices):
    """ Word in String Checker

        A simple way of checking what element of the possible choices list is more similar
         to the user input, in order to have a standard string that will be used as a standard.

        Args:
            user_input (string): user's input string.
            possible_choices ([string]): all possible choices that must be compared.

        Returns:
            possible_element (int): the element of possible choices that
             are similar to the user input.
             The default, if no match occurs, is the first element of the possible choices list.

    """
    user_input = user_input.lower()
    for possible_element in possible_choices:
        if user_input in possible_element:
            return possible_element
    # Default return of first element in the list
    return possible_choices[0]
