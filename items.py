import json
import datetime as dt
import random


class items:
    def __init__(self, activitieType, activitieInit, activitieEnd, activitiePriority, activitieResume, activitieDescription, activitieStatus):
        
        self.activitieType = activitieType
        self.activitieInit = activitieInit
        self.activitieEnd = activitieEnd
        self.activitiePriority = activitiePriority
        self.activitieResume = activitieResume
        self.activitieDescription = activitieDescription
        self.activitieStatus = activitieStatus
        self.activitieId = ()
        pass
        
    def activitieId():
        with open("./Database/itemList.json", "r") as itemList:
            
            while(True):
                id = random.randint(0,5000)
                for item in dict(json.load(itemList))['Activities']:
                    if id != item["id"]:
                        return id
        

    def newActivitie(self):
        id = items.activitieId()
        
        attributesItem = {
            "id" : id,
            "type": self.activitieType,
            "dateInit": self.activitieInit,
            "dateConc": self.activitieEnd,
            "resume": self.activitieResume,
            "priority": self.activitiePriority,
            "description": self.activitieDescription,
            "status": self.activitieStatus
            }
        
        with open('./Database/itemList.json', 'r+', encoding='utf-8') as itemList:
            data = json.load(itemList)
            data['Activities'].append(attributesItem)
            itemList.seek(0)
            json.dump(data, itemList,indent=4, ensure_ascii=False)


