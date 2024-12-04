N = input()
S = input()

t_count = S.count('T')
a_count = S.count('A')

if t_count > a_count :
  print('T')
elif t_count < a_count:
  print('A')
elif t_count == a_count:
  judge = S[-1]
  if judge == 'T':
    print('A')
  else :
    print('T')