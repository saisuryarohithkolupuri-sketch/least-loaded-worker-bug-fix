class LeastLoadedBalancer:

    def __init__(self, workers):

        self.workers = workers

    def get_least_loaded_worker(self):

        sorted_workers = sorted(
            self.workers.items(),
            key=lambda worker: worker[1]
        )

        worker_name = sorted_workers[0][0]

        return worker_name

    def assign_task(self):

        worker = self.get_least_loaded_worker()

        self.workers[worker] += 1

        return worker