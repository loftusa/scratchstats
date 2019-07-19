""" Basic functions. Take in iterators, return scalars. """
import numpy as np
from typing import List, Iterable


def mean(input_data: Iterable) -> float:
    """ 
    Parameters
    ----------
    input_data: Iterable
        np array or list

    Returns
    -------
    float
        Mean of the iterable
    """
    return sum(input_data) / len(input_data)


def median(input_data: Iterable) -> float:
    """ 
    Parameters
    ----------
    input_data: Iterable
        np array or list

    Returns
    -------
    float
        Median of the iterable
    """
    ls = sorted(input_data)
    # if odd, return central number
    if len(ls) % 2 == 1:
        return ls[len(ls) // 2]
    # else if even, return mean of the two central numbers
    else:
        floor = ls[(len(ls) // 2) - 1]
        ceil = ls[len(ls) // 2]
        return mean([floor, ceil])


def _indices_of_ntiles(input_data: Iterable, n: int) -> tuple:
    """Given a List, return n indices, where each index divides the list into a part as evenly as possible.
    
    Parameters
    ----------
    input_data: Iterable
        np array or list

    Returns
    -------
    q_values
        best indices on which to divide evenly
    """
    pass


def quantiles(input_data: Iterable, q_values: tuple) -> List:
    """Given some input data, return a list of lists, where each list is a slice of input_data, using the elements of q_values as the indices for slicing. Divides list into quantiles.
    
    Parameters
    ----------
    input_data: Iterable
        np array or list

    Returns
    -------
    q_subsets: List of Lists, q_values+1 Lists in total.
        
        
    """
    pass


def mode(input_data: Iterable) -> float:
    """ 
    Parameters
    ----------
    input_data: Iterable
        np array or list

    Returns
    -------
    float
        Mode of the iterable
    """
    pass


def ss(input_data: Iterable) -> float:
    pass


def var(input_data: Iterable) -> float:
    pass


def std(input_data: Iterable) -> float:
    pass
