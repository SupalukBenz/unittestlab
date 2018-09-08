def count_unique(list):
  """Count the number of distinct elements in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list

    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
  """
  newlist = []
  for i in list:
    if not i in newlist:
      newlist.append(i)
  return len(newlist)


def binary_search(list, element):
  """Search the index of element in list that already sorted by using Binary Search.
   
    :param list: list of elements for searching
          element: element that want to search index
    :return: the index of element but not found it will return -1
    Examples:
    >>> binary_search([1, 2, 3, 4, 5], 2)
    1
    >>> binary_search([1, 2, 3, 4, 5], 5)
    4
    >>> binary_search([1, 2, 3, 4, 5], 99)
    -1

  """

  if element == None:
        raise TypeError("Search element must not be none")

  first = 0
  last = len(list) - 1
  index = -1
  check_found = False

  while first <= last and not check_found:
    point = (first+last)//2
    if list[point] == element:
      index = point
      check_found = True

    else:
      if element < list[point]:
        last = point - 1
      else:
        first = point + 1
  return index


  