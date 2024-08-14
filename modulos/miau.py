"""
Um módulo de exemplo, com classes, funções e variáveis globais relacionadas a gatos.
"""

from datetime import date

class Gato:
    def __init__(self, nome = '', sexo = '', peso = 0.0, nasc = date.today):
        """nome (str), sexo ('m' ou 'f'), peso (float), nasc (datetime.date)."""
        if sexo not in ('m', 'f'):
            raise Exception("Sexo deve ser 'm' ou 'f'")
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.nasc = nasc

    def __str__(self):
        return '{}, sexo {}, {}Kg, nasceu em {}'.format(
            self.nome, self.sexo, self.peso, self.nasc
        )

    def idade(self):
        """Idade do gato, em anos (float)."""
        return (date.today() - self.nasc).days / 365

um_gato = Gato('Zarabi', 'f', 4.5, date(2010, 9, 4))

def repartir_por_idade(gatos, anos_de_idade):
    gatos_mais_velhos = []
    gatos_mais_novos = []

    for gato in gatos:
        if gato.idade() < anos_de_idade:
            gatos_mais_novos.append(gato)
        else:
            gatos_mais_velhos.append(gato)

    return gatos_mais_velhos, gatos_mais_novos