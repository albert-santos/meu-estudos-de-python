from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")
    def __str__(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")
    def __str__(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)
