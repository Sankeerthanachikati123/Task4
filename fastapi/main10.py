#from fastapi import FastAPI

#database connection
#starlette
#async ,await
#portnumber of react
#template
#websockets
#ginga2 template
#sqlalchemy
#asyncio
#frontend technologies run on which port number
#duplex
#task:to create two sockets where the first message should be displayed on second and viceversa
#semaphore
#concurrency
#thread
#parallelism


import asyncio



'''async def test():
    print("hello")
    await asyncio.sleep(5)
    print("testing.......")
async def run_test():
    await test()
asyncio.run(run_test())'''

async def my():
    print("starting coroutine")
    await asyncio.sleep(10)
    print("resuming.......")

async def main():
    print("starting....")
    await my()
    print("finishiiiiiii")
asyncio.run(main())
