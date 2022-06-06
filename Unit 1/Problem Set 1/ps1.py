###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time
from datetime import datetime

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    finalist = []
    finalist.append([])
    copydict = cows.copy()
    valuelist = list(cows.values())
    currentweight = 0
    currentlist = 0
    while len(copydict.keys()) > 0:
        keystopop = []
        valuetopop = []
        highestweight = max(valuelist)
        for key, value in copydict.items():
            if value == highestweight:
                currentweight += value
                if currentweight <= limit:
                    finalist[currentlist].append(key)
                    valuelist.remove(value)
                    if key not in keystopop:
                        keystopop.append(key)
                if currentweight > limit:
                    finalist.append([])
                    currentlist += 1
                    finalist[currentlist].append(key)
                    valuelist.remove(value)
                    if key not in keystopop:
                        keystopop.append(key)
                    currentweight = value
                try:
                    while True:
                        if min(valuelist) + currentweight <= limit:
                            copyvaluelist = valuelist.copy()
                            for i in range(len(valuelist)):
                                currenthighest = max(copyvaluelist)
                                if currentweight + currenthighest > limit:
                                    copyvaluelist.remove(currenthighest)
                                else:
                                    for key1, value1 in copydict.items():
                                        if value1 == currenthighest and key1 not in keystopop:
                                            finalist[currentlist].append(key1)
                                            valuelist.remove(value1)
                                            if key1 not in keystopop:
                                                keystopop.append(key1)
                                            currentweight += value1
                                            break
                                    break
                        else:
                            break
                except:
                    break
                break
        for element in keystopop:
            copydict.pop(element)
    return finalist


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    keyslist = list(cows.keys())
    minimumtrips = 10
    currentweight = 0
    count = 0
    for item in get_partitions(keyslist):
        for listee in item:
            for element in listee:
                for key, value in cows.items():
                    if key == element:
                        currentweight += value
            if currentweight <= limit:
                count += 1
            currentweight = 0
        if count == len(item) and len(item) <= minimumtrips:
            minimumtrips = len(item)
            result = item.copy()
        count = 0
    return result





# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    '''
    start = time.localtime(time.time())
    x = greedy_cow_transport(cows,10)
    end = time.localtime(time.time())
    converstart = time.asctime(start)
    timestringinit = converstart.split(' ')
    initialtime = timestringinit[3]
    converend = time.asctime(end)
    timestringend = converend.split(' ')
    endtime = timestringend[3]
    format = '%H:%M:%S.%f'
    greedytime = datetime.strptime(initialtime, format) - datetime.strptime(endtime, format)
    '''
    start = time.perf_counter_ns()
    x = greedy_cow_transport(cows,10)
    duration = time.perf_counter_ns() - start
    print(f"Your duration was {duration // 1000000}ms.")
    start1 = time.perf_counter_ns()
    y = brute_force_cow_transport(cows,10)
    duration1 = time.perf_counter_ns() - start1
    print(f"Your duration was {duration1 // 1000000}ms.")
    seconds = (duration1 // 1000000)/1000
    print(f"Your duration was {seconds}s.")
    return


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
#print(greedy_cow_transport({'Rose': 50, 'Lilly': 24, 'Betsy': 65, 'Buttercup': 72, 'Dottie': 85, 'Daisy': 50, 'Willow': 35, 'Coco': 10, 'Abby': 38, 'Patches': 12}, 100))
print(brute_force_cow_transport(cows, limit))
print(compare_cow_transport_algorithms())
