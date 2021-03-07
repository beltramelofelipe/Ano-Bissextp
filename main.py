ano = int(input('Digite um ano: '))

if ano % 4 == 0:
  print('o ano {} é bissexto'.format(ano))
else:
  print('O ano {} não é bissexto'.format(ano))