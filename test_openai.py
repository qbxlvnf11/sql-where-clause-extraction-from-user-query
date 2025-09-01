import os
import openai
from dotenv import load_dotenv

print("--- OpenAI Connection Test ---")

load_dotenv()

# 1. 파이썬이 API 키를 제대로 읽고 있는지 확인
api_key = os.getenv('token') #os.environ.get("OPENAI_API_KEY")
if api_key:
    print("API Key found in environment.")
    # 보안을 위해 키의 일부만 출력
    print(f"Key starts with: {api_key[:5]}...")
else:
    print("Error: OPENAI_API_KEY environment variable not found!")
    # 키가 없으면 테스트 중단
    exit()

# 2. 파이썬이 프록시 설정을 인식하고 있는지 확인
http_proxy = os.environ.get("HTTP_PROXY")
https_proxy = os.environ.get("HTTPS_PROXY")
if http_proxy or https_proxy:
    print(f"HTTP_PROXY found: {http_proxy}")
    print(f"HTTPS_PROXY found: {https_proxy}")
else:
    print("No proxy settings found.")

# 3. OpenAI 클라이언트 초기화 및 API 호출 시도
try:
    print("\nAttempting to create OpenAI client...")
    client = openai.OpenAI(api_key=api_key)
    
    print("Client created. Sending request to chat.completions.create...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Hello world"}]
    )
    
    print("\n--- SUCCESS! ---")
    print("API call was successful.")
    print("Response:", response.choices[0].message.content)

except openai.APIConnectionError as e:
    print("\n--- FAILED: APIConnectionError ---")
    print("Could not connect to OpenAI. This is likely a network issue (firewall, proxy, DNS).")
    print(f"Error details: {e.__cause__}")

except openai.RateLimitError as e:
    print("\n--- FAILED: RateLimitError ---")
    print("Rate limit exceeded. Please check your plan and usage.")

except openai.AuthenticationError as e:
    print("\n--- FAILED: AuthenticationError ---")
    print("Authentication failed. Please check if your API key is correct and active.")

except Exception as e:
    print(f"\n--- FAILED: An unexpected error occurred ---")
    # 전체 에러 트레이스백 출력
    import traceback
    traceback.print_exc()