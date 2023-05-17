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
