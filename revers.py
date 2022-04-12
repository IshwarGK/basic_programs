def FirstReverse(strParam):
  len1 = len(strParam) - 1
  reversStr = ""
  
  while len1 >= 0:
    reversStr = reversStr + strParam[len1]
    len1 = len1 - 1

  # code goes here
  return reversStr

print(FirstReverse("Ishwar"))
