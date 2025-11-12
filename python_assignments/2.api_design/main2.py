"""
2.	Use Jsonplaceholder APIs.
    Please design GET API to retrieve 10 users which should contains the posts they made and the comments they posted and their next to dos

---
In this script, I used `ThreadPoolExecutor` service which manages threads for us and we dont need to manually manage thread like creating, joining and deleting
"""

from fastapi import FastAPI
from concurrent.futures import ThreadPoolExecutor
import requests
import time

app = FastAPI()
base_url = "https://jsonplaceholder.typicode.com"

executor = ThreadPoolExecutor(max_workers=5)


def fetch(endpoint):
    return requests.get(f"{base_url}/{endpoint}").json()


@app.get("/users")
async def get_users():
    """get users"""
    start = time.perf_counter()

    futures = {
        "users": executor.submit(fetch, "users"),
        "posts": executor.submit(fetch, "posts"),
        "comments": executor.submit(fetch, "comments"),
        "todos": executor.submit(fetch, "todos"),
    }

    users = futures["users"].result()
    posts = futures["posts"].result()
    comments = futures["comments"].result()
    todos = futures["todos"].result()

    result = []
    for user in users:
        uid = user["id"]
        user_posts = [p for p in posts if p["userId"] == uid]
        post_ids = [p["id"] for p in user_posts]
        user_comments = [c for c in comments if c["postId"] in post_ids]
        user_todos = [t for t in todos if t["userId"] == uid and not t["completed"]]
        result.append(
            {
                "user_id": uid,
                "name": user["name"],
                "posts": user_posts,
                "comments": user_comments,
                "next_todos": user_todos,
            }
        )

    end = time.perf_counter()
    return {
        "time_taken": round(end - start, 4),
        "user_count": len(result),
        "users": result,
    }


def main():
    print("http://127.0.0.1:8000")
    import uvicorn

    uvicorn.run("main2:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
