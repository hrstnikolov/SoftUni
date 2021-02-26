# jobs = [int(x) for x in input().split(', ')]
# job_index = int(input())
jobs = [3, 1, 10, 1, 2]
job_index = 0
# jobs = [4, 10, 10, 6, 2, 99]
# job_index = 2

sorted_jobs = sorted([(index, job) for index, job in enumerate(jobs)])

clock_cycles = 0
for (index, job) in sorted_jobs:
    clock_cycles += job
    if index == job_index:
        break
        

print(clock_cycles)