import multiprocessing as mp


class Multiprocessing:
    def __init__(self):
        self.job_counter_output = 0

    def calculation(self, n):
        for input_9 in range(n):
            self.job_counter += 1
            print(self.job_counter_output)


cp = Multiprocessing()
p1 = mp.Process(target=cp.calculation, args=(10,))
p2 = mp.Process(target=cp.calculation, args=(70,))
p1.start()
p2.start()
p1.join()
p2.join()
