from analisa_info import analisa_info as anainf #lê os arquivos e suas linhas, armazenando em um dicionário com as informações importantes
#sendo as chaves as colunas e os valores das as linhas da coluna
from abre_arquivos import abre_arquivo as aarq #faz a analise dos dados para obter as estatísticas pedidas nas questões

informacoes = aarq()
anainf(informacoes)