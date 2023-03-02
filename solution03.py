
import numpy as np
import statistics as stat

def mean(elements):
    '''
    Returns the mean of the elements in a list.
    >>>mean([1,3,2])
    2
    '''
    np_elements = np.array(elements)
    np_mean = np.mean(np_elements)
    return np_mean

def median(elements):
    '''
    Returns the median of the elements in a list.
    >>>median([1,2,3])
    2
    '''
    np_elements = np.array(elements)
    np_median = np.median(np_elements)
    return np_median

def mode(elements):
    '''
    Returns the element that appears most in a list.
    >>>mode([1,2,3,1])
    1
    '''
    np_elements = np.array(elements)
    stat_mode = stat.mode(elements)
    return stat_mode

def variance(elements):
    '''
    Returns the variance of elements in a list.
    >>>variance([1,2,3,1])
    0
    '''
    np_elements = np.array(elements)
    stat_variance = stat.variance(np_elements)
    return stat_variance

def number_search(number, elements):
    '''(number, list) -> bool
    Returns True if number in list of elements.
    >>>number_search(1, ['3', '1', '2', '6','0'])
    True
    '''
    for i in elements:
        return str(number) in elements


