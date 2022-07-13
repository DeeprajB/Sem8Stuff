class Job:
    def __init__(self, num, length, deadline):
        self.length = int(length)
        self.deadline = int(deadline)
        self.num = num

    def __str__(self):
        return f"Job_num:{self.num}_len:{self.length}_deadline:{self.deadline}"

    def __repr__(self):
        return f"Job_num:{self.num}_len:{self.length}_deadline:{self.deadline}"


def orderJobs(jobList):
    jobOrder = []
    while(len(jobList) > 0):
        earliestDeadline = 1000000
        earliestJob = -1
        for idx, job in enumerate(jobList):
            if job.deadline < earliestDeadline:
                earliestDeadline = job.deadline
                earliestJob = idx
        jobOrder.append(job)
        del jobList[earliestJob]
    return jobOrder


def feasabilityCheck(jobOrder):
    currTime = 0
    for job in jobOrder:
        currTime += job.length
        if currTime > job.deadline:
            return False
    return True


def main():
    n = int(input("Enter number of jobs: "))
    jobList = []
    for i in range(1, n+1):
        currJob = input(
            f"Enter the length and deadline of job {i} separated by spaces: \n")
        jobList.append(Job(i, *currJob.split(" ")))
    jobOrder = orderJobs(jobList)
    if feasabilityCheck(jobOrder):
        print("Job order will be:")
        for job in jobOrder:
            print(job)
    else:
        print("Jobs cannot be scheduled so all jobs complete before deadline")


main()
