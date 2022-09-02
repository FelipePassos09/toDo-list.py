import json
import datetime as dt
from listItemsOpener import *
import random

class Consulting:
    def __init__(self):
        pass
    
    def consultItems(id = int):
        with open('./Database/itemList.json', 'r', encoding='utf-8') as itemList:
            list = json.load(itemList)
            for document in list['Activities']:
                for (key, value) in document.items():
                    if key == 'id' and value == id:
                        return document
        itemList.close()
    
    def listActivities():
        with open('./Database/itemList.json', 'r', encoding='utf-8') as itemList:
            itemList = json.load(itemList)
            result = []
            
            for item in itemList['Activities']:
                result.append(item)            
            
            return result
    
    def listInitDates():
        with open('./Database/itemList.json', 'r', encoding='utf-8') as itemList:
            itemList = json.load(itemList)
            result = []
            
            for item in itemList['Activities']:
                result.append(item['dateInit'])            
            
            return result
        
    def listEndDates():
        with open('./Database/itemList.json', 'r', encoding='utf-8') as itemList:
            itemList = json.load(itemList)
            result = []
            
            for item in itemList['Activities']:
                result.append(item['dateConc'])            
            
            return result
    
    # def vencItems(prazo = int):
    #     with open('./Database/itemList.json', 'r', encoding='utf-8') as itemList:
    #         itemList = json.load(itemList)
    #         result = []
            
    #         for item in itemList['Activities']:
    #             if dt.datetime.strptime(item['dateConc'],"%y-%m-%d") <= dt.date.today() + dt.timedelta(days= prazo):
    #                 result.append(item)
            
            return result 
    

print(Consulting.consultItems(4380))

            