"""
5.  You are having social network system. Each user relates to different friends.
    You must figure out the path between 2 persons
•   Example. User1 relates to User2 who relates to User3 who relates to User1
•   I prefer the shortest path but consider this as least priority
•   Sample data format is below. Please have nested data format
{
“A”:  [“B”, “C”],
“B”:  [“A”, “D”, “E”],
“C”:  [“A”],
“D”: [“B”],
“E”: [“B”]
}
"""

import json
import time
from collections import deque


def read_input(file_path):
    """read graph from json file"""
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["graph"], data["start"], data["end"], data.get("method", "dfs")


def write_output(file_path, result):
    """write output"""
    with open(file_path, "w") as f:
        json.dump(result, f, indent=4)


def find_path_dfs(graph, start, end, visited=None, path=None):
    """find any path between start and end using DFS."""
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    visited.add(start)

    if start == end:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = find_path_dfs(graph, neighbor, end, visited, path + [neighbor])
            if new_path:
                return new_path
    return None


def find_path_bfs(graph, start, end):
    """find shortest path between start and end using BFS."""
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                queue.append(path + [neighbor])
    return None


def main():
    graph, start, end, method = read_input("input.json")

    start_time = time.time()

    if method.lower() == "bfs":
        path = find_path_bfs(graph, start, end)
        search_method = "BFS"
    else:
        path = find_path_dfs(graph, start, end)
        search_method = "DFS"

    end_time = time.time()
    time_taken = round(end_time - start_time, 6)

    result = {
        "method_used": search_method,
        "graph": graph,
        "start": start,
        "end": end,
        "path_found": path,
        "path_exists": path is not None,
        "path_length": len(path) if path else 0,
        "time_taken_seconds": time_taken,
    }
    output_file_path = "output.json"
    write_output(output_file_path, result)


if __name__ == "__main__":
    main()
