# async/await

# 코루틴(coroutine): 비동기적으로 실행되는 함수(co+routine)
# async def: 키워드로 정의
# 일반 함수는 한 번 실행되면 끝날 때까지 멈추지 않음
# 코루틴은 await를 통해 실행을 양보할 수 있음
# await는 코루틴 내부에서만 사용할 수 있음
# await 뒤에 오는 작업이 완료될 때까지 실행을 잠시 멈추고 다른 코루틴이 실행

import asyncio

# async def로 정의된 코루틴 함수
async def say_after(delay, what):
    print(f"[{what}] 작업을 {delay}초 동안 기다립니다...")
    # await는 실행을 잠시 멈추고 제어권을 반환합니다.
    await asyncio.sleep(delay)
    print(what)

# 메인 코루틴 함수
async def main():
    print("비동기 작업 시작")
    
    # 두 작업을 순차적으로 await
    # 'hello' 작업이 완료될 때까지 'world' 작업은 시작되지 않습니다.
    await say_after(1, 'hello')
    await say_after(2, 'world')
    
    print("비동기 작업 종료")

# asyncio.run()으로 이벤트 루프 시작 및 main 코루틴 실행
if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(main())
    # 코루틴을 실행하는 데 이벤트 루프는 필수
    # await를 통해 실행을 일시 정지하고 제어권을 넘겨주면 누가 실행을 할지 등을 결정하는 주체가 필요
    # asyncio.run()은 비동기 작업을 스케줄링하고 관리하는 이벤트 루프를 자동으로 생성하고 실행
    # 인자로 받은 최상위 코루틴을 실행
    # asyncio.run() 함수는 오직 코루틴 객체만 인자로 받음
    # 따라서 main 함수는 코루틴이어야 함