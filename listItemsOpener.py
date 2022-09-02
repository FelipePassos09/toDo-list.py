import json

class ReadFiles:
    def __init__(self) -> None:
        pass
    
    def openFile():
        with open('./Database/itemList.json', 'r', encoding='utf-8') as itemList:
            return json.load(itemList)