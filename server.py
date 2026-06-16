# 11_[실전 프로젝트] Hello MCP! 프로젝트
# 먼저 두 개의 숫자를 입력받아 사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)을 수행하는 MCP 서버를 만들어보겠습니다. 우선 앞에서 만든 C:\MCP 폴더에 Example-MCP 폴더를 생성한 후 calculator.py 파일을 생성합니다. 그러고 나서 다음과 같은 코드를 작성합니다.

# 01. FastMCP 라이브러리 임포트
# 앞에서 설명했듯이 FastMCP는 MCP 서버를 쉽게 만들 수 있게 해주는 파이썬 라이브러리로서, 
# 여기서는 계산기 기능을 MCP 서버로 제공하기 위해 사용합니다.
from fastmcp import FastMCP

# 02. FastMCP 인스턴스 생성
# FastMCP 인스턴스를 생성합니다. 서버 이름은 "Calculator-MCP"로 지정합니다. 
# 그러고 나면 나중에 클로드 데스크톱에 등록할 때 "Calculator-MCP"라는 이름으로 서버가 저장됩니다.
mcp=FastMCP("Calculator-MCP")


# 03. 계산기 함수 정의 및 데코레이터
@mcp.tool (name="add", description="Add two numbers and return the sum.")
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool (name="sub", description="Subtract the second number from the first.") 
def sub(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool (name="mul", description="Multiply two numbers and return the product.") 
def mul(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool (name="div", description="Divide two numbers (floating point division).") 
def div(a: int, b: int) -> float:
    """Divide two numbers (returns floating point division result)"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    return a / b

# @mcp.tool() 데코레이터를 사용해 각 함수를 MCP 서버의 도구로 등록합니다. 
# 보다시피 사칙연산(add.sub, mul, div) 함수를 통해 각각 덧셈, 뺄셈, 곱셈, 나눗셈(정수 나눗셈)을 수행합니다. 
# 이때 div 함수에서는 나누기 에러를 방지하는 코드를 추가했습니다. 
# 여기서 작성한 함수별 주석(docstring)을 통해 LLM이 각 도구를 인식하게 됩니다.


# 04. 서버 실행 코드
if __name__ == "__main__": 
    mcp.run()

# python calculator.py 명령을 실행하면 MCP 서버를 시작됩니다.

# 이제 calculator.py가 생성된 폴더에서 fastmcp dev inspector calculator.py 명령을 실행하면 
# MCP인스펙터를 통해 각 기능을 직접 테스트해볼 수 있습니다. 
# 이를 통해 앞에서 작성한 사칙연산함수가 정상적으로 동작하는지 손쉽게 확인할 수 있습니다.
