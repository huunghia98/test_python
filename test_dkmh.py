import asyncio
import time
import aiohttp

# Get session browser

cookies = {
    "__RequestVerificationToken": "TnIoWfe3iUafbWa9opGPFdFqphzO5wvbMBIAaZKCUgIKJ7gxDHmBLvyIY1cgiAdNzXLTzG9OjEHlkhiB_7lNpArIc2w1",
    'ASP.NET_SessionId': "fwwvt3escl1dgcoxrtcadqov"
}

list = [653,622]

async def request_site(session, url):
    async with session.post(url) as response:
        print(url,  await response.text())


async def request_list_sites(sites):
    async with aiohttp.ClientSession(cookies=cookies) as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":

    site =  'http://dangkyhoc.vnu.edu.vn/'
    pre_site = [
        'http://dangkyhoc.vnu.edu.vn/danh-sach-mon-hoc/1/1',
        'http://dangkyhoc.vnu.edu.vn/danh-sach-mon-hoc-da-dang-ky/1'
    ]
    pending = []
    confirm = 'http://dangkyhoc.vnu.edu.vn/xac-nhan-dang-ky/1'
    for x in list:
        pending.append(site+f'/chon-mon-hoc/{x}/1/1')
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(request_list_sites(pre_site))

    while True:
        asyncio.get_event_loop().run_until_complete(request_list_sites(pending))
        asyncio.get_event_loop().run_until_complete(request_list_sites([confirm]))
        time.sleep(0.3)

