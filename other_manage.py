"""이 모듈은 other_module의 my_math에서 add 함수를 사용하여 계산을 수행합니다."""

from other_module.my_math import add
import math

calculation_result = add(12, 123123)
calculation_result = add(12, 2)
sqrt_result = math.sqrt(calculation_result)

print(sqrt_result)
print(calculation_result)

# 다른 패키지 사용 예제

# datetime 패키지 사용
from datetime import datetime, timedelta

# 현재 날짜와 시간 출력
현재 = datetime.now()
print(f"현재 날짜와 시간: {현재}")

# 3일 후의 날짜 계산
삼일후 = 현재 + timedelta(days=3)
print(f"3일 후 날짜: {삼일후}")

# random 패키지 사용
import random

# 1부터 100 사이의 랜덤 숫자 생성
랜덤숫자 = random.randint(1, 100)
print(f"생성된 랜덤 숫자: {랜덤숫자}")

# requests 패키지 사용 (설치 필요: pip install requests)
import requests

# 웹 페이지 내용 가져오기
response = requests.get("https://www.example.com")
print(f"웹 페이지 상태 코드: {response.status_code}")
print(f"웹 페이지 내용 일부: {response.text[:100]}...")
