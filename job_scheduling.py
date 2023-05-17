from collections import defaultdict

# Function to schedule the jobs
def printjobschedule(jobs):

    # Create a graph to represent the job dependencies
    graph = defaultdict(list)
    for job in jobs:
        if job[2]:
            graph[job[2]].append(job[0])
