import glob
import os.path
import time
start_time = time.time()

filesList = glob.glob('.\input/*.in')

for fileName in filesList:
    #print(fileName)

    f= open(fileName, 'r')
    maxOutput, no = [int(x) for x in next(f).split()]
    arr = []
    for line in f:
        arr.extend([int(x) for x in line.split()])

    size=len(arr)-1
    maxScore=0
    #print(arr)
    solutionList = []

    for j in range(size,-1,-1):
        total = 0
        currentList = []
        for i in range(j,-1,-1):
            currentValue = arr[i]

            tempSum = total + currentValue

            if tempSum == maxOutput:
                total = tempSum
                currentList.append(i)
                break
            elif tempSum > maxOutput:
                continue
            elif tempSum < maxOutput:
                total = tempSum
                currentList.append(i)

                continue
        if maxScore < total:
            maxScore = total
            #print("Max = "+str(maxScore)+" maxOutput:"+str(maxOutput))
            solutionList = currentList
    outputSize =str(len(solutionList))

    f.close()


    f=open(os.path.join('output', os.path.basename(os.path.splitext(fileName)[0] + '.out')) , 'w')

    output = ' '.join([str(v) for v in solutionList])
    f.write(outputSize+"\n")

    f.write(output)
    f.close()
print("--- %s seconds ---" % (time.time() - start_time))

