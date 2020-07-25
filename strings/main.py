# coding=utf-8
from ExtratoArgumentosUrl import ExtratoArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dólar&valor=1500"

argumentos_url = ExtratoArgumentosUrl(url)
argumentos_url2 = ExtratoArgumentosUrl(url)

valor = argumentos_url.extraiValor()
moedaOrigem, moedaDestino = argumentos_url.ExtraiArgumentos()

print(moedaOrigem, moedaDestino, valor)

urlByteBank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q= https://bytebank.com"
url2 = "https://bytebank.com/cambio/teste/teste"
url3 = "https://bytebank.com/cambio/teste/teste"
# print(url3.startswith(urlByteBank))

print(id(argumentos_url))
print(id(argumentos_url2))
print(argumentos_url == argumentos_url2)