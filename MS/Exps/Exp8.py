# Assume a seek operation takes 3 time units
class Group:
    def __init__(self, name, start):
        self.name = name
        self.jobList = []
        self.start = start

    def __repr__(self):
        return f"Group_{self.name}"

    def __str__(self):
        return f"Group_{self.name}"


class Job:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def __str__(self):
        return f"Job_{self.name}"

    def __repr__(self):
        return f"Job_{self.name}"


start = int(input("Enter start position of disk head: "))
tSlice = int(input("Enter time slice for round robin swapping: "))
n = int(input("Enter number of groups: "))
direction = 1


def init():
    groupList = []
    for i in range(1, n+1):
        group = Group(i, start)
        n_jobs = int(input(f"Enter number of jobs in group {i}: "))
        for j in range(1, n_jobs+1):
            addr = int(input(f"Enter the address of job {j}: "))
            group.jobList.append(Job(j, addr))
        groupList.append(group)
    return groupList


def seekTime(currPos, dest):
    return 3


def SCAN(jobList, currPos):
    global direction
    shortestDis = 100000
    closestJob = -1
    for idx, job in enumerate(jobList):
        dist = abs(currPos-job.addr)
        if direction > 0:
            if job.addr > currPos and dist < shortestDis:
                shortestDis = dist
                closestJob = idx
        else:
            if job.addr < currPos and dist < shortestDis:
                shortestDis = dist
                closestJob = idx
    if idx == -1:
        direction *= -1
        idx = SCAN(jobList, currPos)
    return idx


def schedule(groupList):
    jobOrder = []
    currTime = 0
    currPos = start
    while(len(groupList) > 0):
        for idx, group in enumerate(groupList):
            if len(group.jobList) == 0:
                del groupList[idx]
            else:
                elapsedTime = 0
                while elapsedTime < tSlice:
                    if len(group.jobList) == 0:
                        break
                    idx = SCAN(group.jobList, currPos)
                    job = group.jobList[idx]
                    elapsedTime += seekTime(currPos, job)
                    jobOrder.append(f"{group} {job}")
                    del group.jobList[idx]
                    if elapsedTime >= tSlice:
                        break
    for job in jobOrder:
        print(job)


groupList = init()
schedule(groupList)
