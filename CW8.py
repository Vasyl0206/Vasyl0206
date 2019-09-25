array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]
def count_sheeps(arrayOfSheeps):
  # TODO May the force be with you
    count_num = arrayOfSheeps.count(True)
    return count_num
print (count_sheeps(array1))