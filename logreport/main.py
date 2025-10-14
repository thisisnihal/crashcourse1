from memory_profiler import profile


@profile
def using_json():
    import json
    import heapq
    import time

    start_time = time.perf_counter()

    log_level_freq = {}     # {Key.ERROR: 56, 'WARNING': 12}
    error_service_freq = {} # {'UserService': 12, 'AuthService': 12}
    top_logs = []           # a heap stores top k logs
    top_errors = []         # a heap stores top k error
    log_counter = {}        # {'log_message_x': 2}
    error_counter = {}      # {'error_message_1': 4}
    FILE_PATH = 'data/logs_1000mb.json'
    TOP_K = 5
    class Key:
        LEVEL = 'level'
        ERROR = 'ERROR'
        SERVICE = 'service'
        MESSAGE = 'message'

    f = open(FILE_PATH)
    import json
    logs = json.load(f)
    for index, log in enumerate(logs):
            if log[Key.LEVEL]:
                log_level_freq[log[Key.LEVEL]] = log_level_freq.get(log[Key.LEVEL], 0) + 1
            if log[Key.LEVEL] == Key.ERROR and log[Key.SERVICE]:
                error_service_freq[log[Key.SERVICE]] = error_service_freq.get(log[Key.SERVICE], 0) + 1

            log_key = (log.get(Key.LEVEL,''), log.get(Key.SERVICE,''), log.get(Key.MESSAGE,''))
            log_count = log_counter.get(log_key, 0) + 1

            log_counter[log_key] = log_count
            heapq.heappush(top_logs, (log_count, log_key))
            if len(top_logs) > TOP_K:
                heapq.heappop(top_logs)

            if log.get(Key.LEVEL) == Key.ERROR:
                msg = log.get(Key.MESSAGE,'')
                err_count = error_counter.get(msg, 0) + 1
                error_counter[msg] = err_count
                heapq.heappush(top_errors, (err_count, msg))
                if len(top_errors) > TOP_K:
                    heapq.heappop(top_errors)


    print('log per level:', log_level_freq)
    print('\nerror per service:', error_service_freq)

    most_occured_logs = sorted(top_logs, reverse=True)
    most_occured_errors = sorted(top_errors, reverse=True)

    print("\nmost occured errors: ", most_occured_errors)
    print("\nmost occured logs: ", most_occured_logs)


    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"\nExecution time: {execution_time:.4f} seconds")



@profile
def using_ijson():
    import ijson
    import heapq
    import time

    start_time = time.perf_counter()

    log_level_freq = {}     # {Key.ERROR: 56, 'WARNING': 12}
    error_service_freq = {} # {'UserService': 12, 'AuthService': 12}
    top_logs = []           # a heap stores top k logs
    top_errors = []         # a heap stores top k error
    log_counter = {}        # {'log_message_x': 2}
    error_counter = {}      # {'error_message_1': 4}

    TOP_K = 5
    FILE_PATH = 'data/logs_1000mb.json'
    class Key:
        LEVEL = 'level'
        ERROR = 'ERROR'
        SERVICE = 'service'
        MESSAGE = 'message'

    with open(FILE_PATH, 'r') as f:
        for log in ijson.items(f, 'item'):
            # print(record)
            if log[Key.LEVEL]:
                log_level_freq[log[Key.LEVEL]] = log_level_freq.get(log[Key.LEVEL], 0) + 1
            if log[Key.LEVEL] == Key.ERROR and log[Key.SERVICE]:
                error_service_freq[log[Key.SERVICE]] = error_service_freq.get(log[Key.SERVICE], 0) + 1

            log_key = (log.get(Key.LEVEL,''), log.get(Key.SERVICE,''), log.get(Key.MESSAGE,''))
            log_count = log_counter.get(log_key, 0) + 1

            log_counter[log_key] = log_count
            heapq.heappush(top_logs, (log_count, log_key))
            if len(top_logs) > TOP_K:
                heapq.heappop(top_logs)

            if log.get(Key.LEVEL) == Key.ERROR:
                msg = log.get(Key.MESSAGE,'')
                err_count = error_counter.get(msg, 0) + 1
                error_counter[msg] = err_count
                heapq.heappush(top_errors, (err_count, msg))
                if len(top_errors) > TOP_K:
                    heapq.heappop(top_errors)


    print('log per level:', log_level_freq)
    print('\nerror per service:', error_service_freq)

    most_occured_logs = sorted(top_logs, reverse=True)
    most_occured_errors = sorted(top_errors, reverse=True)

    print("\nmost occured errors: ", most_occured_errors)
    print("\nmost occured logs: ", most_occured_logs)


    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"\nExecution time: {execution_time:.4f} seconds")


if __name__ == '__main__':
    using_json()
    using_ijson()