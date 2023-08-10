import threading
import time

from helper import get_dateTime, get_process_time


class MeatProcessingThread(threading.Thread):
    def __init__(self, meat_queue, worker, lock):
        threading.Thread.__init__(self)

        self.meat_queue = meat_queue  # 佇列，存放待處理的肉資料
        self.worker = worker  # 員工名稱，表示當前處理肉的執行緒
        self.lock = lock  # 用於同步的lock，確保執行緒安全地訪問共享資源

    def run(self):
        while not self.meat_queue.empty():
            # 從佇列中取得待處理的肉
            meat = self.meat_queue.get()

            # 取得鎖，開始執行處理肉的任務
            self.lock.acquire()
            print(f"{self.worker} 在 {get_dateTime()} 取得{meat}")

            # 模擬處理肉所需時間
            time.sleep(get_process_time(meat))

            print(f"{self.worker} 在 {get_dateTime()} 處理完{meat}")

            # 釋放鎖，允許其他執行緒繼續競爭鎖並進入受保護區域操作共享資源
            self.lock.release()
