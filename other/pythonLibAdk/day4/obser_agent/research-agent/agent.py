# https://www.kaggle.com/code/kaggle5daysofai/day-4a-agent-observability
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search

from google.genai import types
from typing import List

from helper import *


import asyncio
# 假设 runner 对象已经被正确初始化

async def main():
    try:
        # 在异步函数内部安全地使用 await
        print("🚀 Running agent with LoggingPlugin...")
        print("📊 Watch the comprehensive logging output below:\n")

        response = await runner.run_debug("Find recent papers on quantum computing")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 使用 asyncio.run() 来运行顶层异步函数
    asyncio.run(main())