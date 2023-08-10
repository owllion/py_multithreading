import threading
from queue import Queue

from thread_manager import (
    populate_meat_queue,
    start_processing_threads,
    wait_for_threads_to_complete,
)


def main():
    meat_queue = Queue()
    thread_pool = []
    lock = threading.Lock()

    populate_meat_queue(meat_queue)
    start_processing_threads(meat_queue, lock, thread_pool)
    wait_for_threads_to_complete(thread_pool)


if __name__ == "__main__":
    main()
