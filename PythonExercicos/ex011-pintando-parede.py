l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))

area = l * h
t = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, h, area))
print('Para pintar a parede, você precisa de {}l de tinta.'.format(t))
