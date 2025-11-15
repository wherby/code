from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.adk.tools import load_memory, preload_memory
from google.genai import types

print("✅ ADK components imported successfully.")

from helper import run_session,retry_config,runner,session_service,APP_NAME,USER_ID
from helper import *





import asyncio
# 假设 runner 对象已经被正确初始化

async def main():
    try:
        # 在异步函数内部安全地使用 await
        # User tells agent about their favorite color
        # Test 1: Tell the agent about a gift (first conversation)
        # The callback will automatically save this to memory when the turn completes
        await run_session(
            auto_runner,
            "I gifted a new toy to my nephew on his 1st birthday!",
            "auto-save-test",
        )

        # Test 2: Ask about the gift in a NEW session (second conversation)
        # The agent should retrieve the memory using preload_memory and answer correctly
        await run_session(
            auto_runner,
            "What did I gift my nephew?",
            "auto-save-test-2",  # Different session ID - proves memory works across sessions!
        )


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 使用 asyncio.run() 来运行顶层异步函数
    asyncio.run(main())