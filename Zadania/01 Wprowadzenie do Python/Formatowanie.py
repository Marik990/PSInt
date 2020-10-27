amount = 100
print('{:4.2f}'.format(amount) + " zł")

temperature = 180
print('{:+d}'.format(temperature))

okrzyk = {'first': 'hip, hip', 'last': 'hurra'}
print('{first}, {last}!'.format(**okrzyk))

print('{first} {last}!'.format(first='STO', last='LAT'))

print('{:{align}{width}}'.format('TYTUŁ', align='^', width='16'))
