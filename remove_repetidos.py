def remove_repetidos(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return sorted(y)

x=eval('[' + input("Digite os números da sua lista separados por vírgula:")+']')

print (remove_repetidos(x))

