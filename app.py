import json
import datetime as dt
import random
import this

class app:
    def __init__(self, *args,):
        self.activitieName = args[0]
        self.activitieType = args[1]
        self.activitieInit = dt.date(args[2])
        self.activitieEnd = dt.date(args[2])
        self.activitiePriority = args[3]
        self.activitieResume = args[4]
        self.activitieDescription = args[5]
        self.activitieStatus = args[6]
        self.activitieId = args[7]
        
    def activitieId():
        with open("./Database/itemList.json", "r") as itemList:
            
            while(True):
                id = random.randint(0,5000)
                for item in dict(json.load(itemList))['Activities']:
                    if id != item["id"]:
                        return id
        

    def newActivitie(type, init, end, priority, resume, description, status):
        id = app.activitieId()
        
        attributesItem = {
            "id" : id,
            "type": type,
            "dateInit": init,
            "dateConc": end,
            "resume": resume,
            "priority": priority,
            "description": description,
            "status": status
            }
        
        with open('./Database/itemList.json', 'r+', encoding='utf-8') as itemList:
            data = json.load(itemList)
            data['Activities'].append(attributesItem)
            itemList.seek(0)
            json.dump(data, itemList,indent=4, ensure_ascii=False)


# Test input parameters:
# tipoItem = "Tarefa"
# dataInicio = str(dt.date(2022, 8, 31))
# activitieEnd = str(dt.date(2022, 8, 31))
# activitiePriority = 'Baixa'
# activitieResume = 'Teste UTF-8'
# activitieDescription = 'ã/õ/í/é/á/ç'
# activitieStatus = 'Success'
        
# app.newActivitie(tipoItem, dataInicio, activitieEnd, activitiePriority, activitieResume, activitieDescription, activitieStatus) 
    
while True:
    tipoItem = input('Que tipo de tarefa pretende criar?  ')
    print('Qual a data de inicio da atividade:  ')
    dataInicio = str(dt.date(
        year = int(input("Ano:  ")),
        month = int(input("Mês:  ")),
        day = int(input("Dia:  "))
    ))
    print('Qual a data de término da atividade: ')
    activitieEnd = str(dt.date(
        year = int(input("Ano:  ")),
        month = int(input("Mês:  ")),
        day = int(input("Dia:  "))
    ))
    activitiePriority = input('Qual a prioridade?  ')
    activitieResume = input('Dê um título para a atividade:  ')
    activitieDescription = input('Descrição da atividade:  ')
    activitieStatus = input('Qual o Status atual da atividade?  ')

    app.newActivitie(tipoItem, dataInicio, activitieEnd, activitiePriority, activitieResume, activitieDescription, activitieStatus)
    
    cont = input('Quer continuar?\n [ S ] = Sim\n [N] = Não\n')
    
    if cont.upper() == 'N':
        break
    
    
print('Done')                
