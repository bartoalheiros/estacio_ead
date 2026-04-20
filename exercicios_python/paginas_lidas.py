import media

total_paginas = int(input('Entre com o número total de páginas: '))
paginas_lidas = 0
percent_lida = 0

paginas_lidas = int(input('Entre com o número de páginas lidas até agora:  '))

percent_lida = (paginas_lidas / total_paginas) * 100

print(f'O percentual de leitura foi: {percent_lida:.2f} %')