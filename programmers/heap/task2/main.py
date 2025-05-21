from dataclasses import dataclass
import heapq
import sys
from typing import Dict, List

'''
디스크 컨트롤러
https://school.programmers.co.kr/learn/courses/30/lessons/42627
'''

@dataclass
class RecordProcess:
    requst_time:int = 0
    finish_time:int = 0

    @property
    def duration_time(self):
        return self.finish_time - self.requst_time


def solution(jobs:List[List[int]]):
    result:Dict[int, RecordProcess] = {}

    # [0] 요청 시각, [1] 작업 번호, [2] 소요시간  
    req_odered_jobs = [(value[0], idx, value[1]) for idx, value in enumerate(jobs)]
    heapq.heapify(req_odered_jobs)

    # [0] 소요시간, [1] 요청 시각, [2] 작업 번호
    ready_queue = []
    
    curr_job = None
    finish_time = -1
    
    time = -1
    while req_odered_jobs or ready_queue:
        
        time += 1

        # 대기 큐에 넣기
        while req_odered_jobs and req_odered_jobs[0][0] == time:
            req_time, job_id, duration_time = heapq.heappop(req_odered_jobs)
            heapq.heappush(ready_queue, (duration_time, req_time, job_id))

        # 현재 job이 없고, 대기 큐에 job이 있는가?
        if not curr_job and ready_queue:
            curr_job = heapq.heappop(ready_queue)
            finish_time = time + curr_job[0]

            #print(f'pop job time({time}) {curr_job} - finish time({finish_time})')
            result[curr_job[2]] = RecordProcess(curr_job[1], finish_time)

        # 작업을 마치지 않았다.
        if curr_job and time < finish_time:
            continue

        # 작업을 맞쳤을 때, 대기큐에 들어와야 할 요청 Job이 있나?
        #print(f'complete job({time} - {finish_time})')
        curr_job = None
        
        while req_odered_jobs and req_odered_jobs[0][0] == time:
            req_time, job_id, duration_time = heapq.heappop(req_odered_jobs)
            heapq.heappush(ready_queue, (duration_time, req_time, job_id))

        # job이 완료 되자마자, 처리 할 job이 있는가? (처리시간은 1ms 이상이므로)
        if not curr_job and ready_queue:
            curr_job = heapq.heappop(ready_queue)
            finish_time = time + curr_job[0]

            #print(f'pop job time({time}) {curr_job} - finish time({finish_time})')
            result[curr_job[2]] = RecordProcess(curr_job[1], finish_time)

    #print(result)

    total_duration_time = sum(map(lambda e : e.duration_time, result.values()))

    return total_duration_time // len(jobs)


def solution_review(jobs:List[List[int]]):

    # 도착 시간, jobId, 소요 시간
    tasks = sorted([(job[0], idx, job[1]) for idx, job in enumerate(jobs)], key=lambda e : (e[0], e[1]))

    ready_queue = []

    first_task = tasks.pop(0)
    ready_queue.append((first_task[2], first_task[0]))

    curr_time = 0
    total_expected_time = 0
    while tasks or ready_queue:
        duration_time, arrival_time = heapq.heappop(ready_queue)

        curr_time = max(curr_time + duration_time, arrival_time + duration_time)

        expect_time = curr_time - arrival_time
        total_expected_time += expect_time

        while tasks and tasks[0][0] <= curr_time:
            next_task = tasks.pop(0)
            heapq.heappush(ready_queue, (next_task[2], next_task[0]))
        
        if tasks and not ready_queue:
            next_task = tasks.pop(0)
            heapq.heappush(ready_queue, (next_task[2], next_task[0]))

    return total_expected_time // len(jobs)



#result = solution_review([[0, 3], [1, 9], [3, 5]]) # 8

result = solution_review([[0, 3], [0, 5], [0, 1]]) # 3
#result = solution([[0, 2], [1, 2], [2, 2], [3, 2]]) # 4 -> 2 아닌가?
#result = solution([[0, 3], [1, 3], [2, 3]]) # 4
#result = solution([[0, 100], [0, 50], [0, 10], [0, 1]]) # 40

print(result)