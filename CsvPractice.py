import matplotlib.pyplot as plt
import csv
import pandas
import re

data = {}
filename = "SalesJan2009.csv"

writefile = "test.csv"
writeLabels = ["Name", "Department", "Favorite Food", "ID"]
writeList = [
    ["Cole", "Math and Computer Science", "Popeyes", 11],
    ["Emma", "Math and Econ", "Might be Popeyes", 26],
    ["Veronika", "Math and Econ", "Dolphinately Popeyes", 7]
]
writeDict = [
    {"Name": "Cole2", "Department": "Math and Computer Science", "Favorite Food": "Popeyes", "ID": 117},
    {"Name": "Emma2", "Department": "Math and Econ", "Favorite Food": "Might be Popeyes", "ID": 268},
    {"Name": "Veronika2", "Department": "Math and Econ", "Favorite Food": "Dolphinately Popeyes", "ID": 73}
]

def noModuleRead():
    '''
        This reads a csv file into a dictionary
        without any modules: note the removal of
        quotes and commas
    '''
    data = {}
    with open(filename, "r") as f:
        csvLines = f.readlines()
        for label in csvLines[0].strip().split(','):
            data[label] = []
        for line in csvLines[1:]:
            # get rid of quotation marks/in-field commas
            offset = 0
            while line.find('"') != -1:
                firstInd = line.find('"', offset)
                secondInd = line.find('"', firstInd+1)
                offset = secondInd+1
                if secondInd != -1:
                    middle = line[firstInd:secondInd].replace(',', '').replace('"', '').strip()
                    diff = len(line[firstInd:secondInd]) - len(middle)
                    offset += diff
                    line = line[:firstInd] + middle + line[secondInd+1:]
            # add entry to dictionary at proper field
            for entry, label in zip(line.split(','), data.keys()):
                data[label].append(entry.strip())
    return data

def noModuleWrite():
    '''
        This writes sample csv data to a file
        without any modules
    '''
    with open(writefile, "w") as f:
        f.write(','.join(writeLabels) + "\n")
        # writing from lists
        for line in writeList:
            f.write(','.join([str(entry) for entry in line]) + "\n")
        # writing from dicts
        for line in writeDict:
            f.write(','.join([str(line[label]) for label in writeLabels]) + "\n")

def csvModuleRead():
    '''
        This reads a csv file into a dictionary
        with the csv module
    '''
    data = {}
    with open(filename, "r") as f:
        csvLines = csv.DictReader(f)
        labels = False
        for line in csvLines:
            # initialize key-value pairs in dict
            if not labels:
                labels = True
                for label in line:
                    data[label] = [line[label]]
            else:
                # add new entries
                for label in data.keys():
                    data[label].append(line[label].strip())
    return data

def csvWrite():
    '''
        This writes sample csv data to a file
        with the csv module
    '''
    with open(writefile, "w") as f:
        # writing from lists
        csvWriter = csv.writer(f)
        csvWriter.writerow(writeLabels)
        csvWriter.writerows(writeList)
        # writing from dicts
        csvWriter = csv.DictWriter(f, fieldnames=writeLabels)
        csvWriter.writerows([entry for entry in writeDict])

def pandasRead():
    '''
        This reads a csv file into a dictionary
        with the pandas module
    '''
    data = {}
    df = pandas.read_csv(filename)
    data.update(df)
    return data

def pandasWrite():
    '''
        This writes sample csv data to a file
        with the pandas module
    '''
    # writing from list
    df = pandas.DataFrame(writeList, columns=writeLabels)
    # writing from dicts
    df = df.append(pandas.DataFrame(writeDict, columns=writeLabels), ignore_index=True)
    df.to_csv(writefile, index=False)

def printEntry(index):
    '''
        prints the entry at a passed index
    '''
    print(f"\nPrinting entry {index}:")
    for label in data.keys():
        print(label, ":", data[label][index])

def getAvgPriceForCard():
    '''
        This returns a dictionary where each key corresponds
        to a card type, and we have a list for the value
        where the first index is average price and the second
        is the number of data points (non-numeric chars removed)
    '''
    paymentToCard = {}
    # use regex to get rid of in-field commas
    intPrice = lambda price : int(re.sub('[^0-9]+', '', str(price)))
    for price, card in zip(data["Price"], data["Payment_Type"]):
        if card not in paymentToCard:
            paymentToCard[card] = [intPrice(price), 1]
        else:
            # sum prices per card
            paymentToCard[card][0] += intPrice(price)
            paymentToCard[card][1] += 1
    # divide each sum by number of points
    for card in paymentToCard:
        paymentToCard[card][0] /= paymentToCard[card][1]
    return paymentToCard

def plotStuffMPL():
    '''
        plots average payment by card (matplotlib)
    '''
    cards = avgPayment.keys()
    avg = [ avgPayment[card][0] for card in avgPayment ]
    padding = (max(avg) - min(avg)) / 2
    plt.ylim(min(avg) - padding, max(avg) + padding)
    plt.bar(cards, avg)
    plt.ylabel('Average Payment')
    plt.xlabel('Card')
    plt.title('Average Payment by Card')
    plt.show()

def plotStuffPD():
    '''
        plots average payment by card (matplotlib and pandas)
    '''
    df = pandas.DataFrame(avgPayment)
    row = df.iloc[0]
    row.plot.bar()
    plt.ylabel('Average Payment')
    plt.clabel('Card')
    plt.title('Average Payment by Card')
    plt.show()

if __name__ == "__main__":
    # Testing our three methods of reading!
    data = noModuleRead()
    printEntry(3)
    data = csvModuleRead()
    printEntry(3)
    data = pandasRead()
    printEntry(3)
    # Use our data to plot something!
    avgPayment = getAvgPriceForCard()
    plotStuffMPL()
    plotStuffPD()
    # Write some CSV to a file
    noModuleWrite()
    csvWrite()
    pandasWrite()