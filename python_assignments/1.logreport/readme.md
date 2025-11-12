### Problem 
1.You are given a raw log file which contains messages in JSON format.

Example: `{“timestamp”: “2025-10-13 20:05:05”, “level”: “ERROR”, “message”: “DB failed to connect”, “service”: “UserService”}`

The log file could be very large also in GBs.  
Please create a report which contains with the following:  
•	Count of errors per service  :done
•	Most common error messages  
•	Count of each log levels  :done
•	Most 5 occurred logs with their count  

---


` .\.logreportenv\Scripts\activate`

### Run with memory profiler
` python -m memory_profiler .\main.py`


https://stackoverflow.com/questions/10382253/reading-rather-large-json-files

http://pypi.python.org/pypi/ijson/

https://pythonspeed.com/articles/json-memory-streaming/