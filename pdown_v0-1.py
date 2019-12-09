import asyncio
import concurrent.futures
import urllib.request
import time

URL = "http://127.0.0.1:8081/"
THREADS = 1000

def make_the_request(current_url):
    res = urllib.request.urlopen(current_url).read()
    if b"ql" in res:
        print('Found Error stacktrace !')
        with open("save_%d.html" % req_id, "wb") as f:
            f.write(res)
    #else:
    #    print('No stacktrace found... ')

async def main():

    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                make_the_request, 
                URL
            )
            for i in range(THREADS)
        ]
        for response in await asyncio.gather(*futures):
            pass
    end = time.time()
    msg = 'Operation took {:.3f} seconds to complete.'
    print(msg.format(end-start))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())