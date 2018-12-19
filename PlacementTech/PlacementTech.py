### FIRST FIT ###
class FirstFit: 
    def __init__(self, partitions, jobs):
        self.partitions = partitions
        self.jobs = jobs
        self.manged = []
        self.fitted = False

    def replace(self, old, new):
        i = self.partitions.index(old)
        self.partitions.remove(old)
        self.partitions.insert(i, new)

    def assigning(self):
        for j in self.jobs:
            self.fitted = False
            for p in self.partitions:
                if p >= j:
                    self.manged.append([j, p])
                    self.replace(p, p-j)
                    self.fitted = True
                    break
            if (not self.fitted):
                self.manged.append([j, 'must wait'])
        return self.manged

######################################################################################

### BEST FIT ###
class BestFit: 
    def __init__(self, partitions, jobs):
        self.partitions = partitions
        self.jobs = jobs
        self.manged = []
        self.fitted = False

    def replace(self, old, new):
        i = self.partitions.index(old)
        self.partitions.remove(old)
        self.partitions.insert(i, new)

    def assigning(self):
        self.partitions.sort()
        for j in self.jobs:
            self.fitted = False
            for p in self.partitions:
                if p >= j:
                    self.manged.append([j, p])
                    self.replace(p, p-j)
                    self.fitted = True
                    break
            if (not self.fitted):
                self.manged.append([j, 'must wait'])
        return self.manged

######################################################################################

### WORST FIT ###
class WorstFit: 
    def __init__(self, partitions, jobs):
        self.partitions = partitions
        self.jobs = jobs
        self.manged = []
        self.fitted = False

    def replace(self, old, new):
        i = self.partitions.index(old)
        self.partitions.remove(old)
        self.partitions.insert(i, new)

    def assigning(self):
        self.partitions.sort(reverse=True)
        for j in self.jobs:
            self.fitted = False
            for p in self.partitions:
                if p >= j:
                    self.manged.append([j, p])
                    self.replace(p, p-j)
                    self.fitted = True
                    break
            if (not self.fitted):
                self.manged.append([j, 'must wait'])
        return self.manged
            
######################################################################################

### NEXT FIT ###
class NextFit: 
    def __init__(self, partitions, jobs):
        self.partitions = partitions
        self.jobs = jobs
        self.manged = []
        self.fitted = False

    def replace(self, old, new):
        i = self.partitions.index(old)
        self.partitions.remove(old)
        self.partitions.insert(i, new)

    def assigning(self):
        pointer = 0
        for j in self.jobs:
            self.fitted = False
            for i in range(pointer, len(self.partitions)):
                p = self.partitions[i]
                if p >= j:
                    self.manged.append([j, p])
                    pointer = i
                    self.replace(p, p-j)
                    self.fitted = True
                    if pointer >= len(self.partitions):
                        pointer = 0
                    break
            if (not self.fitted):
                self.manged.append([j, 'must wait'])
        return self.manged

###################################################################################

def run(obj):
    obj.assigning()
    obj.show()

def show(manged): 
    print()
    for x in manged:
        print('job {} => {}'.format(x[0], x[1]))

def check(item, li):
    for x in li:
        if item > x:
            return True
    return False

partitionsNo = int(input('enter partitions number: '))
partitions = []
for x in range(partitionsNo):
    partition = int(input('enter partition #{} size: '.format(x)))
    partitions.append(partition)

jobsNo = int(input('\nenter jobs number: '))
jobs = []
i=0
while i < jobsNo:
    job = int(input('enter job #{} size: '.format(x)))
    if check(job, partitions) == False:
        jobs.append(job)
        i+=1
    else:
        print('job cant fit in any')

while True:
    print('\nenter number of placment technology: \n1-First Fit \n2-Next Fit \n3-Best Fit \n4-Worst Fit')
    choice = int(input('--> '))
    if choice == 1:
        show(FirstFit(partitions, jobs).assigning()) 
        break
    elif choice == 2:
        show(NextFit(partitions, jobs).assigning())  
        break
    elif choice == 3:
        show(BestFit(partitions, jobs).assigning())  
        break
    elif choice == 4:
        show(WorstFit(partitions, jobs).assigning())  
        break
    else:
        print('wrong choice')



