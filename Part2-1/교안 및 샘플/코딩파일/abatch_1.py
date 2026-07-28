
import asyncio
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
# 1. 언어 모델과 프롬프트 정의
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
prompt = ChatPromptTemplate.from_template("{product}를 만드는 회사의 이름을 추천해줘")

# 2. LCEL 체인 구성 (프롬프트 | 모델)
chain = prompt | llm

# 3. 비동기 함수 정의
async def main():
    # 여러 입력 데이터 준비
    products = [
        {"product": "친환경 물병"},
        {"product": "스마트 커피 머신"},
        {"product": "컬러풀한 양말"}
    ]
    
    # abatch 메서드를 사용하여 비동기적으로 실행
    results = await chain.abatch(products)
    
    # 결과 출력
    for result in results:
        print(result.content)

# 4. 비동기 함수 실행
if __name__ == "__main__":
    asyncio.run(main())