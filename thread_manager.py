from helper import get_number_of_meat, meat_types, workers
from worker_thread import MeatProcessingThread


def populate_meat_queue(meat_queue):
    for meat in meat_types:
        for _ in range(get_number_of_meat(meat)):
            meat_queue.put(meat)


def start_processing_threads(meat_queue, lock, thread_pool):
    for worker in workers:
        thread = MeatProcessingThread(meat_queue, worker, lock)
        thread_pool.append(thread)
        thread.start()


def wait_for_threads_to_complete(thread_pool):
    for thread in thread_pool:
        thread.join()
