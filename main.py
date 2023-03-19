# python3

# python3

# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    start_times= [0] * n
    thread_heaps=[(0,i) for i in range (n)] 

    for i in range(m):
        processing_time=data[i]

        free_time, thread_idx=heapq.heappop(thread_heaps)

        output.append((thread_idx, free_time))

        start_times[thread_idx]=free_time+processing_time

        heapq.heappush(thread_heaps,(start_times[thread_idx],thread_idx))


   

    return output


def main():
   # n = 0
   # m = 0

    n,m=map(int, input().split())

    
    data = [int(x) for x in input().split()]

    result = parallel_processing(n,m,data)
    
    

    for a,start_time in result:
        print(a,start_time)



if _name_ == "_main_":
    main()

