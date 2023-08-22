def rang(a):
  ans = '('
  if(len(a) == 1):
    i = 0
    while(i < a[0]):
      if(round(i) == round(i, 4)):
        ans += str(round(i)) + '.0, '
      else:
        ans += str(round(i, 4)) + ', '
      i += 1
  elif(len(a) == 2):
    i = a[0]
    while(i < a[1]):
      if(round(i) == round(i, 4)):
        ans += str(round(i)) + '.0, '
      else:
        ans += str(round(i, 4)) + ', '
      i += 1
  else:
    i = a[0]
    while(i < a[1]):
      if(round(i) == round(i, 4)):
        ans += str(round(i)) + '.0, '
      else:
        ans += str(round(i, 4)) + ', '
      i += a[2]

  ans = ans[:-2] + ')'
  return ans


if __name__ == '__main__': 
  print("*** New Range ***")
  a = [float(x) for x in input("Enter Input : ").split()]
  print(rang(a))