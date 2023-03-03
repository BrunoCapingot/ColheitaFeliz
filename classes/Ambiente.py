"""
Import de de todas as classes para centralizar as inicializações
"""
from classes import Areas,Banco,Biblioteca,classeEtapa

class Ambiente():
    def __init__(self,etapa):
        self.etapa = etapa
        self.classesPorEtapa = {0:'Classes para etapa 0'}


    def definicaoDeAmbiente(self):
        """
        Define classes a serem inicializadas apartir da etapa que o jogador esta
        """
        return self.classesPorEtapa[self.etapa]
