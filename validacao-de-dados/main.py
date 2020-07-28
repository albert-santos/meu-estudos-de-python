from TelefonesBr import TelefonesBr
import re
from datetime import datetime, timedelta
from DatasBr import DatasBr
from acesso_cep import BuscaEndereco

#cpf_um = "15316264754"
#print(cpf_um)

#exemplo_cnpj = "35379838000112"
#exemplo_cpf = "11"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
#documento = Documento.cria_documento(cpf_um)
#print(documento)

'''
padrao = "[0-9][a-z]{2}[0-9]"
texto = "123 1aa2 342"
resposta = re.search(padrao, texto)
print(resposta.group())
'''
'''
padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "alkodk albert123@gmail.com.br"
resposta = re.search(padrao, texto)
print(resposta.group())
'''

'''
padrao_molde = "(xx)aaaa-www"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "meus numeros são 91234568796 91987654857"
resposta = re.findall(padrao, texto)
print(resposta)
'''
'''
telefone = "559163574985"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
'''
'''
cadastro = DatasBr()
print(cadastro.dia_semana())
'''

'''
cadastro = DatasBr()
print(cadastro)
'''

'''
hoje = DatasBr()
print(hoje.tempo_cadastro())
'''

cep = "12340987"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
