import requests
from threading import Thread
import logging
import time

logging.basicConfig(
    filename="app.log", 
    level = logging.INFO, 
    filemode='w')

def get_job(descript, page):
    r = requests.get("https://jobs.github.com/positions.json", params={"description":descript, "page":page})
    logging.info("URL: %s", r.url)

description = ["python", "java", "c#"]
threads = []
pages = [1,2]
for a in description:
    for page in pages:
        threads.append(Thread(target = get_job, args = (a, page)))

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

logging.info("Время выполнения: %s" % str(end-start))