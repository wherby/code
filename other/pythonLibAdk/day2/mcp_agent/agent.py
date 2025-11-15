import uuid
from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from google.adk.apps.app import App, ResumabilityConfig
from google.adk.tools.function_tool import FunctionTool

print("✅ ADK components imported successfully.")


retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)


# MCP integration with Everything Server
mcp_image_server = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",  # Run MCP server via npx
            args=[
                "-y",  # Argument for npx to auto-confirm install
                "@modelcontextprotocol/server-everything",
            ],
            tool_filter=["getTinyImage"],
        ),
        timeout=30,
    )
)

print("✅ MCP Tool created")

# Create image agent with MCP integration
image_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="image_agent",
    instruction="Use the MCP Tool to generate images for user queries",
    tools=[mcp_image_server],
)

from google.adk.runners import InMemoryRunner

runner = InMemoryRunner(agent=image_agent)



from IPython.display import display, Image as IPImage
import base64

import asyncio
# 假设 runner 对象已经被正确初始化

async def main():
    try:
    #     # 在异步函数内部安全地使用 await
    #     response = await currency_runner.run_debug(
    # "I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?"
    # )   
        # Test the enhanced agent
        response = await runner.run_debug("Provide a sample tiny image", verbose=True)
        print(response)
        for event in response:
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, "function_response") and part.function_response:
                        for item in part.function_response.response.get("content", []):
                            if item.get("type") == "image":
                                display(IPImage(data=base64.b64decode(item["data"])))
        #print(response)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 使用 asyncio.run() 来运行顶层异步函数
    asyncio.run(main())


