a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(len(d)) #mostrará  o tamanho da tupla
print(c.count(5)) #contará quantos termos entre () tem na Tupla
print(c.index(8)) #index = qual posição está o termo entre ()
print(d.index(2))
print(d.index(2, 4)) #index = posição do termo apartir da posição 4 DESLOCAMENTO