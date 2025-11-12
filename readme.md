
# Projects

## 1. Infinite Scroll 
It is a simple react webapp which load random images from unsplash api via a fastapi proxy server.  
To run the application:

1. **Frontend:**

   * Go to `/infinitescroll/frontend` and run `npm run dev` to start the React frontend.

2. **Backend:**

   * Since the frontend communicates with a proxy API (not the Unsplash API directly), you need to run the backend.  
   * Go to the `/infinitescroll/backend` directory and execute to start the backend.:  
    ```
    python infinitescroll.py
    ```


## 2. Draggable  
It is a simple kanban board which uses HTML Drag & Drop API.  
To run the application:

1. **Frontend:**

   * Navigate to `/draggable/` and run `npm run dev` to start the React frontend.

## 3. Json Log report Analysis
A script that analyses the log report stored in a json file format.  

The Json file can be in GBs so using `json` can be bottleneck for smaller machines(say 512gb ram server).  

So I used one external python library called `ijson` which parses the json file iteratively. Meaning it loads one item of a json file in memory at a time.  

To run it with memory profiler (inside `logreport` directory):
```
python -m memory_profiler json_logreport_mem_profiler.py
```  
I have also provided one jupyter notebook file(`research.ipynb` inside `logreport` directory) to run and test for different files.  


## 4. browser-extensions-manager-ui-main
This one is basically a challenge from https://www.frontendmentor.io, in it I tried to clone a particular webpage.  

So I used reactjs and tailwindcss for this project.  
To run it, go inside `browser-extensions-manager-ui-main`  and run
```
npm i
npm run dev
```  
* I also deployed the static build on my digitalocean instance and it is live at: http://blog.hostthis.tech/extensions/


## 5. ApiDesign
**Problem statement:** Use Jsonplaceholder APIs.  Please design GET API to retrieve 10 users which should contains the posts they made and the comments they posted and their next to dos
- Navigate to `/ApiDesign` directory  
There are two python files `main1.py` and `main2.py`  
`main1.py` is using `threading` and rely on manual thread management on the other hand `main2.py` is using `ThreadPoolExecutor` which manages thread for us.

