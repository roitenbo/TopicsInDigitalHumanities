import csv
import io

if __name__ == '__main__':
    f = open("list.txt", "r+",encoding="utf8")
    s = f.read();
    a = s.split("\n");
    lines = []
    for an in a:
        anList = list(an)
        index = 0
        for c in an:
            if c == '[' or c == ']':
                anList[index] = '|'
            index += 1
        an = "".join(anList)
        lines.append(an.split('|'))
        #print(an)

    index = 1
    nIndex = 1
    total = ""
    #print('9' >= '0' and '9' <= '9')
    for l in lines:
        if(l[0] >= '0' and l[0] <= '9'):
            l[0] = index.__str__()
            index += 1
            if(len(l) > 1):
                l[len(l)-1] = "נ/"+nIndex.__str__()
                nIndex += 1
            #print(l[len(l)-1])
        if(len(l) > 1):
            #print(l)
            total += "|".join(l) + "\n"
    #print(("").join(total))
    newList = total.split('\n')
    tsvFile = ""
    newListIndex = 0
    prev = 0

    noSeperator = []


    for a in newList:
        noSeperator.append(a.split("|"))

    for a in newList:
        #print("newLine")
        quoteIndex = 0
        withoutSeperator = a.split("|")
        #print(withoutSeperator)
        for b in withoutSeperator:
            #print("b = ",b)
            if b.replace(" ","") == '"' or b.replace(" ","") == '"""':
                print("newListIndex = ",newListIndex,"quoteIndex = ",quoteIndex)
                b = noSeperator[newListIndex-1][quoteIndex]
                noSeperator[newListIndex][quoteIndex] = b
                print (b)
            tsvFile += b + "\t"
            quoteIndex += 1
        newListIndex += 1

        tsvFile += "\n"
    f.close();

    with io.open('ocr.tsv', "w",encoding="utf-8") as tsv:
        tsv.write(tsvFile)
    tsv.close()


