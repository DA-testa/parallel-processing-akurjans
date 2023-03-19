# python3

# python3

import heapq


def parallel_processing(n, m, data):
    output = []
    start_times = [0] * num_threads
    thread_heap = [(0, i) for i in range(num_threads)]
    

    for i in range(num_jobs):
        processing_time = job_times[i]

        free_time, thread_idx = heapq.heappop(thread_heap)
        
        output.append((thread_idx, free_time))

        start_times[thread_idx] = free_time + processing_time

        heapq.heappush(thread_heap,(start_times[thread_idx], thread_idx))
    return output

def main():
    
    num_threads, num_jobs = map(int, input().split())

    job_times = [int(x) for x in input().split()]

    result = parallel_processing(num_threads, num_jobs, job_times)

    for thread_idx, start_time in result:
        print(thread_idx, start_time)
    

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
