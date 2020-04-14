from sklearn.ensemble import RandomForestClassifier
import numpy as np

domainlist = []
class Domain:
    def __init__(self,_name,_label,_length,_countofnum):
        self.name=_name
        self.label=_label
        self.length=_length
        self.countofnum=_countofnum

    def returnData(self):
        return [self.length,self.countofnum]
        
    def returnLabel(self):
        if self.label=="dga":
             return 1
        else:
             return 0

def return_num_number(string):
    num_number = 0
    for char in string:
        if char.isdigit():
            num_number += 1
    return num_number


def initData(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line =="":
                continue
            tokens = line.split(",")
            name=tokens[0]
            label=tokens[1]
            length=len(tokens[0])
            countofnum=return_num_number(tokens[0])
            domainlist.append(Domain(name,label,length,countofnum))

def main():
    initData("train.txt")
    featureMatrix =[]
    labelList = []
    for item in domainlist:
        featureMatrix.append(item.returnData())
        labelList.append(item.returnLabel())

    clf = RandomForestClassifier(random_state=0)
    clf.fit(featureMatrix,labelList)
    
    result=open("result.txt","w")
    with open("test.txt") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line =="":
                continue
            tokens = line.split(",")
            name=tokens[0]
            length=len(tokens[0])
            countofnum=return_num_number(tokens[0])
            
            result.write(name)
            result.write(',')
            if clf.predict([[length,countofnum]])==1:
                result.write('dga\n')
            else:
                result.write('notdga\n')
    print("finished")

            





if __name__ =='__main__':
    main()





