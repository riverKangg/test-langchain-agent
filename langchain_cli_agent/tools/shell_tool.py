# tools/shell_tool.py
import subprocess
from langchain.tools import tool

@tool
def shell_tool(command: str) -> str:
    """쉘 명령어를 실행하고 결과를 반환합니다. 예: 'ls -l'"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            executable="/bin/bash",  # <== 이 줄 추가
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip() or result.stderr.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"
