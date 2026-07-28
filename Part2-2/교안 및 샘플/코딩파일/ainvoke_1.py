# ainvoke
# 단일 입력에 대해 비동기적으로(asynchronously) 체인을 실행
# I/O 작업이 많은 환경에서 유용하며, 작업이 완료될 때까지 다른 작업을 계속 처리할 수 있음
# ainvoke는 async/await 문법과 함께 사용

import asyncio
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

# 1. 언어 모델과 프롬프트 정의
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
prompt = ChatPromptTemplate.from_template("{product}를 만드는 회사의 이름을 추천해줘")

# 2. LCEL 체인 구성
chain = prompt | llm

# 3. 비동기 함수 정의
async def main():
    # 단일 입력 데이터 준비
    data = {"product": "친환경 물병"}
    
    # ainvoke 메서드를 사용하여 비동기적으로 실행
    # await 키워드를 사용해야 합니다.
    result = await chain.ainvoke(data)
    
    # 결과 출력
    print(result.content)

# 4. 비동기 함수 실행
if __name__ == "__main__":
    asyncio.run(main())