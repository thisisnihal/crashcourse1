


`uvicorn main:app --reload --port 8000`






```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def my_context():
    print("Before yield (setup)")
    yield
    print("After yield (cleanup)")

async def main():
    async with my_context():
        print("Inside context (doing work)")

```
output:
```
Before yield (setup)
Inside context (doing work)
After yield (cleanup)
```