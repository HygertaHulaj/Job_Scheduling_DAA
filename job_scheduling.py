from collections import defaultdict

# Function to schedule the jobs
def printjobschedule(jobs):

    # Create a graph to represent the job dependencies
    graph = defaultdict(list)
    for job in jobs:
        if job[2]:
            graph[job[2]].append(job[0])
        else:
            graph[None].append(job[0])

    # Sort jobs by their deadlines in increasing order
    jobs = sorted(jobs, key=lambda x: x[1])
   
    
    # Keep track of the earliest deadline and the time required to complete each job
    earliest_deadline = {job[0]: job[1] for job in jobs}
    time_required = {job[0]: job[1] for job in jobs}

    
    # Schedule jobs in the order of their deadlines
    schedule = []
    for _ in range(len(jobs)):
        # Find the job with the earliest deadline that has all dependencies scheduled
        job = None
