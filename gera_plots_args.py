import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def create_directory(path):
    """Cria um diretório se ele não existir."""
    if not os.path.exists(path):
        os.makedirs(path)

print('Quantidade de argumentos:', len(sys.argv), 'argumentos.')
print('Lista de argumentos:', sys.argv)
print('Argumento 0 sys.argv[0]:', sys.argv[0])
print('Argumento 1 sys.argv[1]:', sys.argv[1])

def plota_pivot_table(df, valor, índice, func, ylabel , xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=valor, index=índice, aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'classificar':
        pd.pivot_table(df, values=valor, index=índice, aggfunc=func).sort_values(valor).plot(figsize=[15, 5])
    elif opcao == 'desempilhar':
        pd.pivot_table(df, values=valor, index=índice, aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None

sinasc = pd.read_csv('SINASC_RO_2019_' + sys.argv[1] + '.csv')
print('Dados mínimos: ', sinasc.DTNASC.min())
print('Dados máximos: ', sinasc.DTNASC.max())
max_data = sinasc.DTNASC.max()[:7]
print(max_data)

# Verifique e crie o diretório antes de salvar
output_directory = '../output/figs/'
create_directory(output_directory)

plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'count', 'quantidade de nascimento', 'data de nascimento')
plt.savefig(output_directory + 'quantidade de nascimento_' + max_data + '.png')

plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae', 'data de nascimento', 'unstack')
plt.savefig(output_directory + 'media idade mae por sexo_' + max_data + '.png')

plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe', 'data de nascimento', 'unstack')
plt.savefig(output_directory + 'media peso bebe por sexo_' + max_data + '.png')

plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'apgar1 mediano', 'gestacao', 'sort')
plt.savefig(output_directory + 'apgar1 mediano por escolaridade mae_' + max_data + '.png')

plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 médio', 'gestacao', 'sort')
plt.savefig(output_directory + 'media apgar1 por gestacao_' + max_data + '.png')

plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 médio', 'gestacao', 'sort')
plt.savefig(output_directory + 'media apgar5 por gestacao_' + max_data + '.png')

