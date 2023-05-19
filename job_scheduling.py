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
        for j in jobs:
            if j[0] not in schedule and all(dependency in schedule for dependency in graph[j[0]]):
                if job is None or earliest_deadline[j[0]] < earliest_deadline[job]:
                    job = j[0]
        schedule.append(job)
        for successor in graph[job]:
            earliest_deadline[successor] = min(earliest_deadline[successor], earliest_deadline[job] - time_required[job])
        time_required.pop(job)
 

    # Print the schedule
    print(schedule)


    # Driver
    jobs = []

     n = int(input("Enter the number of jobs: "))
     for i in range(n):

        
        job_name = input(f"Enter the name of job {i+1}: ")
        job_time = int(input(f"Enter the time required for job {i+1}: "))
        dependency = input(f"Enter the dependency for job {i+1} (leave empty if none): ")
        jobs.append((job_name, job_time, dependency))

print("Minimum time to complete all jobs is achieved by the following schedule:")
printjobschedule(jobs)


