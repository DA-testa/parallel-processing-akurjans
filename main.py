# python3
import heapq


def parallel_processing(n_threads, n_jobs, job_times):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    
    thread_times = [0] * n_threads 
    for i in range(n_jobs):
        thread_idx = thread_times.index(min(thread_times))
        output.append((thread_idx, thread_times[thread_idx]))
        thread_times[thread_idx] += job_times[i]
    return output

def main():
    # TODO: create input from keyboard
    
    
    # n_threads - thread count 
    # n_jobs - job count
    n_threads, n_jobs = map(int, input().split())

   
    
    job_times = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n_threads, n_jobs, job_times)
    
    # TODO: print out the results, each pair in it's own line
    for thread_idx, start_time in result:
        print(thread_idx, start_time)

if __name__ == "__main__":
    main()

