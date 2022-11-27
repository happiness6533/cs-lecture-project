import heapq


def reverse_single_job(single_job):
    return [single_job[1], single_job[0]]


def solution(jobs):
    priority_queue = []

    jobs.sort()
    single_job = jobs[0]
    total_time = single_job[1]
    total_wait_and_do_time = single_job[1]
    for i in range(len(jobs)):
        # 대기시간(작업 하나 마칠때마다 바뀜) + 작업시간 이 최소인 작업을 뽑아서 먼저 처리한다
        heapq.heappush(priority_queue, [])








        heapq.heappush(priority_queue, reverse_single_job(jobs[i]))

    total_time = 0
    total_wait_and_do_time = 0

    print(priority_queue, jobs, total_time, total_wait_and_do_time)
    single_job = heapq.heappop(priority_queue)
    jobs.remove(reverse_single_job(single_job))
    total_time += single_job[0]
    total_wait_and_do_time += single_job[0]
    while priority_queue:
        find_wait_job_flag = False
        for i in range(len(jobs)):
            if jobs[i][0] < total_time:
                find_wait_job_flag = True
                break
        print(priority_queue, jobs, total_time, total_wait_and_do_time)

        if find_wait_job_flag:
            single_job = heapq.heappop(priority_queue)
            jobs.remove(reverse_single_job(single_job))
            total_wait_and_do_time += (total_time - single_job[1] + single_job[0])
            total_time += single_job[0]
        else:
            single_job = jobs[0]
            priority_queue.remove(reverse_single_job(single_job))
            jobs.remove(single_job)
            total_wait_and_do_time += single_job[1]
            total_time = single_job[0] + single_job[1]
    print(priority_queue, jobs, total_time, total_wait_and_do_time)

    print(total_wait_and_do_time // len_job)
    return total_wait_and_do_time // len_job


solution([[0, 3], [1, 9], [2, 6]])
