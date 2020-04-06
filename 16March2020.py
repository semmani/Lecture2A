import pandas as pd
import numpy as np

dataSet  = pd.DataFrame()

dataSet['Outlook'] = ['sunny','sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy',
                      'sunny', 'overcast','overcast','rainy']
dataSet['Temperature'] = ['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild',
                      'mild', 'mild','hot','mild']

dataSet['Humidity'] = ['high','high','high','high','normal','normal','normal','high','normal','normal','normal',
                       'high','normal','high']
dataSet['Windy'] = ['false','true','false','false','false','true','true','false','false','false','true',
                       'true','false','true']
dataSet['Play'] = ['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']

print(dataSet)
print(type(dataSet['Play']))


def computeEntropyOfPlay():
    total = len(dataSet['Play'])
    numOfYes =  len(dataSet[dataSet['Play'] ==  'yes'])
    numOfNo =  len(dataSet[dataSet['Play'] ==  'no'])
    print(numOfYes)
    print(numOfNo)
    probabilityOfYes = numOfYes / total
    probabilityOfNo = numOfNo / total
    print(probabilityOfYes)
    print(probabilityOfNo)

    Entropy1 = -(probabilityOfYes * np.log2(probabilityOfYes))-(probabilityOfNo * np.log2(probabilityOfNo))
    #Entropy = -(len(dataSet[dataSet['Play'] ==  'yes'])/len(dataSet['Play']))* (np.log2(len(dataSet[dataSet['Play'] ==  'yes'])/len(dataSet['Play'])))-((len(dataSet[dataSet['Play'] ==  'no'])/len(dataSet['Play']))* (np.log2((len(dataSet[dataSet['Play'] ==  'no']))/len(dataSet[dataSet['Play']]))
    return Entropy1

def computeEntropyOfOutlook():
    print("\n Entropy of Outlook------>")
    total = len(dataSet['Outlook'])
    numOfSunny =  len(dataSet[dataSet['Outlook'] ==  'sunny'])
   # dataSet['Outlook'] = dataSet['Play'].map('Play')
    #print(dataSet)
    #  if dataSet['Outlook'] == 'sunny' and dataSet[]
    #print(dataSet)
    numOfOvercast =  len(dataSet[dataSet['Outlook'] ==  'overcast'])
    numOfRainy = len(dataSet[dataSet['Outlook'] == 'rainy'])
    print(numOfSunny)
    print(numOfOvercast)
    print(numOfRainy)
    probabilityOfSunny = numOfSunny / total
    probabilityOfOvercast = numOfOvercast / total
    probabilityOfRainy = numOfRainy / total
    print("Calculating Entropy ")
    SunnyYes = 2 / numOfSunny
    print(SunnyYes)
    SunnyNo = 3 / numOfSunny
    EntropySunny = -((SunnyYes) * np.log2(SunnyYes)) - ((SunnyNo) * np.log2(SunnyNo))
    print("E(S): ",EntropySunny.__round__(2))
    OvercastYes = 4 / numOfOvercast
    OvercastNo = 0 / numOfOvercast
    EntropyOvercast = -((OvercastYes) * np.log2(OvercastYes)) - 0
    print("E(O): ", EntropyOvercast.__round__())
    RainyYes = 3 / numOfRainy
    RainyNo = 2 / numOfRainy
    EntropyRainy = -((RainyYes) * np.log2(RainyYes)) - ((RainyNo) * np.log2(RainyNo))
    print("E(R): ", EntropyRainy.__round__(2))

    print("Information From Outlook---->>")
    info = (numOfSunny / total * EntropySunny) + (numOfOvercast/ total * EntropyOvercast) + (numOfRainy/ total * EntropyRainy)
    #print(info)
    return info


def computeTempOutlook():
    print("Entropy of temperature---->")
    total = len(dataSet['Temperature'])
    numOfHot = len(dataSet[dataSet['Temperature'] == 'hot'])
    numOfMild = len(dataSet[dataSet['Temperature'] == 'mild'])
    numOfCool = len(dataSet[dataSet['Temperature'] == 'Cool'])
    probabilityOfHot = numOfHot / total
    probabilityOfMild = numOfMild / total
    probabilityOfCool = numOfCool / total

    print("Calculating Entropy ")
    HotYes = 2 / numOfHot
    HotNo = 2 / numOfHot
    EntropyHot = -((HotYes) * np.log2(HotYes)) - ((HotNo) * np.log2(HotNo))
    print("E(H): ", EntropyHot.__round__(2))
    MildYes = 4 / numOfMild
    MildNo = 2 / numOfMild
    EntropyMild = -((MildYes) * np.log2(MildYes)) - ((MildNo) * np.log2(MildNo))
    print("E(M): ", EntropyMild.__round__())
    CoolYes = 3 / numOfCool
    CoolNo = 1 / numOfCool
    EntropyCool = -((CoolYes) * np.log2(CoolYes)) - ((CoolNo) * np.log2(CoolNo))
    print("E(C): ", EntropyCool.__round__(2))

    print("Information From Outlook---->>")
    info = (numOfHot / total * EntropyHot) + (numOfMild / total * EntropyMild) + (
                numOfCool / total * EntropyCool)
    # print(info)
    return info



   # EntropyOfSunny = -(probabilityOfSunny * np.log2(probabilityOfSunny))-(probabilityOfNo * np.log2(probabilityOfNo))
    #Entropy = -(len(dataSet[dataSet['Play'] ==  'yes'])/len(dataSet['Play']))* (np.log2(len(dataSet[dataSet['Play'] ==  'yes'])/len(dataSet['Play'])))-((len(dataSet[dataSet['Play'] ==  'no'])/len(dataSet['Play']))* (np.log2((len(dataSet[dataSet['Play'] ==  'no']))/len(dataSet[dataSet['Play']]))
    #return Entropy

def computeGainOutlook():
    entropy1 = computeEntropyOfPlay()
    infoGainOutlook = computeEntropyOfOutlook()
    infoGainTemp = computeTempOutlook()

    GainEntropy = entropy1 - infoGainTemp
    print("Gain(Outlook): ", GainEntropy)




computeEntropyOfPlay()
computeEntropyOfOutlook()
computeGainOutlook()

