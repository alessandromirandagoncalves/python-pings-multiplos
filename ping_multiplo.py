#########################################################
# Alessandro Miranda Gonçalves                          #
# Linkedin: www.linkedin.com/alessandromirandagoncalves #
# Março/2022                                            #
#########################################################
# O arquivo hosts.csv tem 2 colunas separadas por vírgula:
# a primeira coluna informa o nome do host ou IP
# a segunda coluna informa a quantidade de pacotes a serem transmitidos
# desta forma, pode-se personalizar o "Ping" para cada destino

import os       #Biblioteca que permite usar funções de rede
import re       #Biblioteca que checa strings com expressões regulares
import time     #Biblioteca com funções de tempo
import csv      #Biblioteca de funções para ler aquivos CSV

print ('Programa Pings múltiplos')
print(50 * '-')

lista = []
contador = 0

with open('hosts.csv', newline='') as csvfile:
    linha = csv.reader(csvfile, delimiter=',') # separado por vírgula

    # o módulo csv lerá todas as linhas
    for i in linha:
        lista.append(i)
        host = lista[contador][0]
        pacotes = lista[contador][1]
        contador += 1
        # Testa a sintaxe válida para IP/Host
        # Verifica formato IP válido. Ex: 192.0.0.1
        sintaxe_ip = re.search(
            '^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})$', host)
        ##Verifica formato HOST válido. Ex: www.seati.ma.gov.br
        sintaxe_host = re.search(
            '^(http[s]?://|ftp://)?(www\.)?[a-zA-Z0-9-\.]+\.(com|org|net|mil|edu|ca|co.uk|com.au|gov|br)$', host)
        ## Se não tem IP ou host válido, exibe mensagem e despreza
        if sintaxe_ip == None and sintaxe_host == None:
            print('IP/Host inválido: {}. Procurando próximo...\n'.format(host))
        else:
            ## Mensagem personalizada se for host
            if sintaxe_ip == None:
                print('Verificando host: {} com {} pacotes'.format(host,pacotes))
            ## Mensagem personalizada se for IP
            else:
                print('Verificando IP: {} com {} pacotes'.format(host,pacotes))
            os.system('ping -n {} {}\n'.format(pacotes,host))
            print(50 * '-')
            time.sleep(5)