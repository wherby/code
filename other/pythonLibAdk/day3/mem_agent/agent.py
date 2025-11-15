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
        response = await run_session(
    runner,
    "My favorite color is blue-green. Can you write a Haiku about it?",
    "conversation-01",  # Session ID
)
        session = await session_service.get_session(
            app_name=APP_NAME, user_id=USER_ID, session_id="conversation-01"
        )

        # Let's see what's in the session
        print("📝 Session contains:")
        for event in session.events:
            text = (
                event.content.parts[0].text[:60]
                if event.content and event.content.parts
                else "(empty)"
            )
            print(f"  {event.content.role}: {text}...")
        # This is the key method!
        await memory_service.add_session_to_memory(session)
        await run_session(runner, "What is my favorite color?", "color-test")
        await run_session(runner, "My birthday is on March 15th.", "birthday-session-01")

        # Manually save the session to memory
        birthday_session = await session_service.get_session(
            app_name=APP_NAME, user_id=USER_ID, session_id="birthday-session-01"
        )

        await memory_service.add_session_to_memory(birthday_session)
        print("✅ Session added to memory!")

        print("✅ Birthday session saved to memory!")

        # Test retrieval in a NEW session
        await run_session(
            runner, "When is my birthday?", "birthday-session-02"  # Different session ID
        )

        # Search for color preferences
        search_response = await memory_service.search_memory(
            app_name=APP_NAME, user_id=USER_ID, query="What is the user's favorite color?"
        )

        print("🔍 Search Results:")
        print(f"  Found {len(search_response.memories)} relevant memories")
        print()

        for memory in search_response.memories:
            if memory.content and memory.content.parts:
                text = memory.content.parts[0].text[:80]
                print(f"  [{memory.author}]: {text}...")


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 使用 asyncio.run() 来运行顶层异步函数
    asyncio.run(main())