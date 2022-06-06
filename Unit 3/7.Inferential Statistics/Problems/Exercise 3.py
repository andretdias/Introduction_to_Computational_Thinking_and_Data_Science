from cmath import nan


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    mean = 0
    elementsum = 0
    if len(L) == 0:
        return float("nan")
    else:
        for element in L:
            mean += len(element)
        mean = mean/len(L)
        for element in L:
            elementsum += (len(element) - mean)**2
    stdeviation = (elementsum / len(L))**(1/2)
    return stdeviation