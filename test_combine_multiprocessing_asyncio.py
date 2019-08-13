# import requests
# import multiprocessing
# import time
#
# session = None
#
# import asyncio
# import time
# import aiohttp
#
# session = ''
#
# async def download_site(session, url):
#     async with session.get(url) as response:
#         print("Read {0} from {1}".format(response.content_length, url))
#
#
# async def download_all_sitessss(sites):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in sites:
#             task = asyncio.ensure_future(download_site(session, url))
#             tasks.append(task)
#         await asyncio.gather(*tasks, return_exceptions=True)
#
#
# def set_global_session():
#     global session
#     if not session:
#         session = requests.Session()
#
# def down(sites):
#     asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
#
# def download_all_sites(sites):
#     with multiprocessing.Pool(initializer=set_global_session) as pool:
#         pool.map(down, sites)
#
#
# if __name__ == "__main__":
#     sites = [
#                 "https://www.jython.org",
#                 "http://olympus.realpython.org/dice",
#             ] * 80
#     print(len(sites))
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")
