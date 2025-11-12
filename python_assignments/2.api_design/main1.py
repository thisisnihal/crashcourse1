"""
2.	Use Jsonplaceholder APIs.
    Please design GET API to retrieve 10 users which should contains the posts they made and the comments they posted and their next to dos
"""

from fastapi import FastAPI
import requests
import threading
import time

app = FastAPI()
base_url = "https://jsonplaceholder.typicode.com"

data_store = {}
lock = threading.Lock()


def fetch(endpoint):
    resp = requests.get(f"{base_url}/{endpoint}")
    with lock:
        data_store[endpoint] = resp.json()


@app.get("/users")
def get_users():
    start = time.perf_counter()

    endpoints = ["users", "posts", "comments", "todos"]

    threads = []

    for ep in endpoints:
        t = threading.Thread(target=fetch, args=(ep,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    users = data_store["users"][:10]
    posts = data_store["posts"]
    comments = data_store["comments"]
    todos = data_store["todos"]

    result = []

    for user in users:
        user_id = user["id"]
        user_posts = [p for p in posts if p["userId"] == user_id]
        user_post_ids = [p["id"] for p in user_posts]
        user_comments = [c for c in comments if c["postId"] in user_post_ids]
        user_next_todos = [
            t for t in todos if t["userId"] == user_id and not t["completed"]
        ]

        result.append(
            {
                "user_id": user_id,
                "name": user["name"],
                "posts": user_posts,
                "comments": user_comments,
                "next_todos": user_next_todos,
            }
        )

    end = time.perf_counter()
    print(f"time_taken_sec: {round(end - start, 4)}")
    return {
        "time_taken_sec": round(end - start, 4),
        "user_count": len(result),
        "users": result,
    }


def main():
    print("http://127.0.0.1:8000")
    import uvicorn

    uvicorn.run("main1:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
