def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        combo = []
        combo.append([])
        combo.append([])
        for j in range(N):
            if (i//3**j) % 3 == 1:
                combo[0].append(items[j])
            if (i//3**j) % 3 == 2:
                combo[1].append(items[j])
        Combo = tuple(combo)
        yield Combo


list1 = (1,2,3)
test1 = yieldAllCombos(list1)

print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
print(test1.__next__())
