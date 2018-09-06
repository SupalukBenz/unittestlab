def count_unique(list_element):
  copylist = []

  for a in list_element:
    copylist.append(a)

  for i in set(copylist):
    copylist.remove(i)
  copylist = list(set(copylist))
            
  return len(copylist)
