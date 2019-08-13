import time
from celery import group
from celery_worker import download


sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

start_time = time.time()
res = group(download.s(site) for site in sites)()
middle_time = time.time()
print(middle_time-start_time)
res.get()
duration = time.time() - start_time
print(f"Downloaded {len(sites)} in {duration} seconds")