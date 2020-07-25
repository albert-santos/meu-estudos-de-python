frase = 'Curso em Vídeo Python'
print(frase[0:15:2])

print("""The mere mention of Brazil brings to mind sun, fun and samba.
But there are a whole lot of other things the country does particularly well.
Here are ten things done better in Brazil than anywhere else.""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase)
'''frase = frase.replace('Python', 'Androide')
print(frase)'''
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido[2])
print(dividido[2][3])