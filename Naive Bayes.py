# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:15:40 2019

@author: ilhamksyuriadi
"""

import xlrd

def LoadDataset(FileLoc):
    data = []
    label = []
    workbook = xlrd.open_workbook(FileLoc)
    sheet = workbook.sheet_by_index(0)
    for i in range(1,sheet.nrows):
        data.append([sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3),sheet.cell_value(i,4),sheet.cell_value(i,5),sheet.cell_value(i,6),sheet.cell_value(i,7)])
        label.append(sheet.cell_value(i,8))
    return data,label

def ClassProbability(label):
    more,less = 0,0
    for i in range(len(label)):
        if label[i] == '>50K':
            more += 1
        else:
            less += 1
    return more/160,less/160

def CountProbability(data,col,label,more,less):
    allAtt = []
    for i in range(len(data)):
        if data[i][col] not in allAtt:
            allAtt.append(data[i][col])
    Att1More = str(allAtt[0]) + '>50K'
    Att1Less = str(allAtt[0]) + '<=50K'
    Att2More = str(allAtt[1]) + '>50K'
    Att2Less = str(allAtt[1]) + '<=50K'
    Att3More = str(allAtt[2]) + '>50K'
    Att3Less = str(allAtt[2]) + '<=50K'
    prob = {}
    for i in range(len(data)):
        if data[i][col] == allAtt[0]:
            if label[i] == '>50K':
                if Att1More in prob:
                    prob[Att1More] += 1
                else:
                    prob[Att1More] = 1
            elif label[i] == '<=50K':
                if Att1Less in prob:
                    prob[Att1Less] += 1
                else:
                    prob[Att1Less] = 1
        elif data[i][col] == allAtt[1]:
            if label[i] == '>50K':
                if Att2More in prob:
                    prob[Att2More] += 1
                else:
                    prob[Att2More] = 1
            elif label[i] == '<=50K':
                if Att2Less in prob:
                    prob[Att2Less] += 1
                else:
                    prob[Att2Less] = 1
        elif data[i][col] == allAtt[2]:
            if label[i] == '>50K':
                if Att3More in prob:
                    prob[Att3More] += 1
                else:
                    prob[Att3More] = 1
            elif label[i] == '<=50K':
                if Att3Less in prob:
                    prob[Att3Less] += 1
                else:
                    prob[Att3Less] = 1
    prob[Att1More] = prob[Att1More] / more
    prob[Att1Less] = prob[Att1Less] / less
    prob[Att2More] = prob[Att2More] / more
    prob[Att2Less] = prob[Att2Less] / less
    prob[Att3More] = prob[Att3More] / more
    prob[Att3Less] = prob[Att3Less] / less
    return prob

def Classifier(data,age,work,edu,married,occu,relation,hour,more,less):
    predict = []
    for i in range(len(data)):
        predictM = age[data[i][0]+'>50K'] * work[data[i][1]+'>50K'] * edu[data[i][2]+'>50K'] * married[data[i][3]+'>50K'] * occu[data[i][4]+'>50K'] * relation[data[i][5]+'>50K'] * hour[data[i][6]+'>50K'] * more
        predictL = age[data[i][0]+'<=50K'] * work[data[i][1]+'<=50K'] * edu[data[i][2]+'<=50K'] * married[data[i][3]+'<=50K'] * occu[data[i][4]+'<=50K'] * relation[data[i][5]+'<=50K'] * hour[data[i][6]+'<=50K'] * less
        if predictM > predictL:
            predict.append('>50K')
        elif predictL > predictM:
            predict.append('<=50K')
    return predict

def Accuracy(actual,predict):
    count = 0
    for i in range(len(predict)):
        if predict[i] == actual[i]:
            count += 1
    return count / len(predict) * 100
        
data,label = LoadDataset('Trainset.xlsx')
more,less = ClassProbability(label)
age = CountProbability(data,0,label,more,less)
work = CountProbability(data,1,label,more,less)
edu = CountProbability(data,2,label,more,less)
married = CountProbability(data,3,label,more,less)
occu = CountProbability(data,4,label,more,less)
relation = CountProbability(data,5,label,more,less)
hour = CountProbability(data,6,label,more,less)
predict = Classifier(data,age,work,edu,married,occu,relation,hour,more,less)
print(Accuracy(label,predict))
















