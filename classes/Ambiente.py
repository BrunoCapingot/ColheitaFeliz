"""
Import de de todas as classes para centralizar as inicializações
"""

from Areas import Area
from Bancos import Banco
from Bibliotecas import Biblioteca
from Inventarios import Inventario
from Lojas import Loja
from Pesquisas import Pesquisa
from Players import Player
from Tempos import Tempo

class Ambiente():
    def __init__(self,etapa):
        self.etapa = etapa
        self.classesPorEtapa = {
            0:'Classes para etapa 0',
            1:'Classes para etapa 1',
            2:'Classes para etapa 2',
            3:'Classes para etapa 3',
                                }


    def definicaoDeAmbiente(self):
        """
        Define classes a serem inicializadas apartir da etapa que o jogador esta
        """
        return self.classesPorEtapa[self.etapa]
