 #! multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
 #!                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
 #!                   multithreading = better for io bound tasks (waiting around)


from multiprocessing import Process, cpu_count
import time

def counter(num):
    count= 0
    while count<num:
        count+=1

def main():

    print("cpu count:", cpu_count()) #! printing the number of CPU's

    #! As there are 4 processor counts in my computer so if i create more than 4 processes it might take longer then expected

    a = Process(target=counter, args=(100,))
    b = Process(target=counter, args=(100,))

    a.start()
    b.start()

    print("processing...")

    a.join()
    b.join()


    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")



if __name__ == '__main__':  #If using windows need to do this.
    main()