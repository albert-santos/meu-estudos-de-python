import re

email1 = "Meu numero é 91234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular 91234-1234"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao,email3)
print(retorno)
