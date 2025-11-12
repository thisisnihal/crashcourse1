"""
1. You are given a raw log file which contains messages in JSON format.
Example:  {“timestamp”: “2025-10-13 20:05:05”, “level”: “ERROR”, “message”: “DB failed to connect”, “service”: “UserService”}
The log file could be very large also in GBs.
Please create a report which contains with the following
•	Count of errors per service
•	Most common error messages
•	Count of each log levels
•	Most 5 occurred logs with their count
"""

import ijson
import heapq
import time

TOP_K = 5
FILE_PATH = "data/logs_1000mb.json"


class Key:
    LEVEL = "level"
    ERROR = "ERROR"
    SERVICE = "service"
    MESSAGE = "message"


def process_logs(file_path):
    log_level_freq = {}  # {Key.ERROR: 56, 'WARNING': 12}
    error_service_freq = {}  # {'UserService': 12, 'AuthService': 12}
    log_counter = {}  # {'log_message_x': 2}
    error_counter = {}  # {'error_message_1': 4}

    with open(file_path, "r") as f:
        for log in ijson.items(f, "item"):
            if log[Key.LEVEL]:
                log_level_freq[log[Key.LEVEL]] = (
                    log_level_freq.get(log[Key.LEVEL], 0) + 1
                )
            if log[Key.LEVEL] == Key.ERROR and log[Key.SERVICE]:
                error_service_freq[log[Key.SERVICE]] = (
                    error_service_freq.get(log[Key.SERVICE], 0) + 1
                )

            log_key = (
                log.get(Key.LEVEL, ""),
                log.get(Key.SERVICE, ""),
                log.get(Key.MESSAGE, ""),
            )
            log_counter[log_key] = log_counter.get(log_key, 0) + 1

            if log.get(Key.LEVEL) == Key.ERROR:
                msg = log.get(Key.MESSAGE, "")
                error_counter[msg] = error_counter.get(msg, 0) + 1

    return log_level_freq, error_service_freq, log_counter, error_counter


def get_top_k(counter_dict, k):
    return heapq.nlargest(k, counter_dict.items(), key=lambda x: x[1])


def main():
    start_time = time.perf_counter()

    log_level_freq, error_service_freq, log_counter, error_counter = process_logs(
        FILE_PATH
    )
    top_logs = get_top_k(log_counter, TOP_K)
    top_errors = get_top_k(error_counter, TOP_K)

    print("log per level:", log_level_freq)
    print("\nerror per service:", error_service_freq)
    print("\nmost occured errors:", sorted(top_errors, reverse=True))
    print("\nmost occured logs:", sorted(top_logs, reverse=True))

    end_time = time.perf_counter()
    print(f"\nExecution time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()
