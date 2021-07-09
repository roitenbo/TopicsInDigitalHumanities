# -*- coding: utf-8 -*-

import csv

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', family='Arial')

if __name__ == '__main__':
    edot = {
    }
    f = open("update.tsv", "r+",encoding="utf8")
    read_tsv = csv.reader(f, delimiter="\t")
    name = ""
    for row in read_tsv:
        name = row[4][::-1]
        if name in edot:
            edot[name] += 1
        elif not (row[4] == '' or row[4] == 'religion'):
            edot[name] = 1
    #print(edot)

    plt.bar(edot.keys(), edot.values())
    plt.title('עדות ברשימה' [::-1])
    plt.xlabel('עדה' [::-1])
    plt.ylabel('כמות' [::-1])
    pic = plt.gcf()
    plt.show()
    plt.draw()
    pic.savefig('edot.png', dpi=100)

    print("as da= ")

    f = open("update.tsv", "r+",encoding="utf8")
    read_tsv = csv.reader(f, delimiter="\t")

    fellNames = []

    gil = {
        "לפנ" : 0 ,
        "0-1" : 0 ,
        "1-2": 0,
        "2-3": 0,
        "3-4": 0,
        "4-5": 0,
        "5-6": 0,
        "6-7": 0,
        "7-8": 0,
        "8-9": 0,
    }
    second = ""
    for row in read_tsv:
        if row[5] == 'נפל':
            second = row[5][::-1]
            gil[second] += 1
            fellNames.append(int(row[0]))
        elif not (row[5] == '' or row[5] == 'age' or row[5] == '-') :
            #print(row[5])
            second = row[5][2]
            if second == '3':
                gil["2-3"] += 1
            elif second == '5':
                num = float(row[5][0:3])
                #print(num)
                gil["0-1"] += 1
            else:
                if second == 'י' :
                    gil["0-1"] += 1
                if second == 'ש' :
                    if len(row[5]) == 3: #years
                        year = row[5][0] + "-" + str(int(row[5][0]) + 1)
                        gil[year] += 1
                    else: #weeks
                        gil["0-1"] += 1
                if second == 'ח' :
                    gil["0-1"] += 1

    print(gil)

    plt.bar(gil.keys(), gil.values())
    plt.title('גיל ברשימה' [::-1])
    plt.xlabel('טווח גיל - שנים' [::-1])
    plt.ylabel('כמות' [::-1])
    pic = plt.gcf()
    plt.show()
    plt.draw()
    pic.savefig('gil.png', dpi=100)


    f = open("update.tsv", "r+",encoding="utf8")
    read_tsv = csv.reader(f, delimiter="\t")

    names = {
    }
    lastName = {
    }
    finalLastName = {
    }
    second = ""
    for row in read_tsv:
        print(row[3])
        name = row[3][::-1]
        if not (row[3] == '' or row[3] == 'lastName' or row[3] == '-') :
            if name in lastName:
                lastName[name] += 1
                names[row[3]] += " , " + row[1]
            else:
                lastName[name] = 1
                names[row[3]] = row[1]

    for l in lastName.keys():
        if(lastName[l]>1):
            finalLastName[l[len(l)-1]]=lastName[l]
            #print(l)

    plt.bar(finalLastName.keys(), finalLastName.values())
    plt.title('קשרי שמות משפחה' [::-1])
    plt.xlabel('שם משפחה' [::-1])
    plt.ylabel('כמות' [::-1])
    pic = plt.gcf()
    plt.show()
    plt.draw()
    pic.savefig('lastName.png', dpi=1000)


    for n in names.keys():
        if not n == '':
            opp = n[::-1]
            if lastName[opp]>1:
                print("share lastName ", n , " :\t" , names[n])


    f = open("update.tsv", "r+",encoding="utf8")
    read_tsv = csv.reader(f, delimiter="\t")

    #print(fellNames)
    words = ["num: ","name: ","fatherName: ","lastName: ","religion: ","age: ","case: "]
    i = 0
    for row in read_tsv:
        if not (row[0] == '' or row[0] == 'num'):
            if int(row[0]) in fellNames:
                for word in row:
                    if not word == '':
                        print ( words[i] + word + " \t\t\t ",end='')
                        i += 1
                i = 0
                print()


