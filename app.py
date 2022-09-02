from items import *
from consulting import *

#Test input parameters:
# tipoItem = "Tarefa"
# dataInicio = str(dt.date(2022, 8, 31))
# activitieEnd = str(dt.date(2022, 8, 31))
# activitiePriority = 'Baixa'
# activitieResume = 'Teste UTF-8'
# activitieDescription = 'ã/õ/í/é/á/ç'
# activitieStatus = 'Success'
        
# newItem = items(activitieType = tipoItem, activitieInit= dataInicio, activitieEnd= activitieEnd,activitiePriority= activitiePriority,  activitieResume= activitieResume, activitieDescription= activitieDescription, activitieStatus= activitieStatus)


while True:
    print(f'Bem vindo ao seu gerenciador de tarefas!\n{"-/" *20}-\nPor onde deseja começar:\n')
    options = ['[ 1 ] - Consultar items.',
               '[ 2 ] - Resumo de atividades planejadas.',
               '[ 3 ] - Resumo de atividades atrasadas.',
               '[ 4 ] - Inserir um novo item.'
               ]
    
    for item in options: print(item, end='\n')
    choose = int(input("Escolha uma opção:  "))
    
    if choose == 4:
        while True:
            tipo = input('Que tipo de tarefa pretende criar?  ')
            print('Qual a data de inicio da atividade:  ')
            dataIni = str(dt.date(
                year = int(input("Ano:  ")),
                month = int(input("Mês:  ")),
                day = int(input("Dia:  "))
            ))
            print('Qual a data de término da atividade: ')
            dataFim = str(dt.date(
                year = int(input("Ano:  ")),
                month = int(input("Mês:  ")),
                day = int(input("Dia:  "))
            ))
            prioridade = input('Qual a prioridade?  ')
            resumo = input('Dê um título para a atividade:  ')
            descricao = input('Descrição da atividade:  ')
            status = input('Qual o Status atual da atividade?  ')

            newItem = items(activitieType = tipo, activitieInit= dataIni, activitieEnd= dataFim,activitiePriority= prioridade,  activitieResume= resumo, activitieDescription= descricao, activitieStatus= status)
            
            
            save = input("Salvar atividade?\n [ S ] = Sim\n [ N ] = Não\n")
            if save.upper() == 'S':
                items.newActivitie(newItem)
            
            cont = input('Quer continuar?\n [ S ] = Sim\n [ N ] = Não\n')
            
            if cont.upper() == 'N':
                break
    
    if choose == 1:
        while True:
            print('[ 1 ] Consultar um item especifico:')
            print('[ 2 ] Ver a lista de items')
            print('[ 3 ] Ver os items a vencer')
            
            choose = int(input("Insira a opção desejada:  "))
        
        
            cont = input('Quer continuar?\n [ S ] = Sim\n [ N ] = Não\n')
                
            if cont.upper() == 'N':
                break


    cont = input('Quer continuar?\n [ S ] = Sim\n [ N ] = Não\n')
                
    if cont.upper() == 'N':
        break 
            
        
    
    
print('Done')                
