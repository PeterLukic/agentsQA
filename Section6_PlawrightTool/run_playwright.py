from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_sync_playwright_browser

sync_browser = create_sync_playwright_browser(headless=True)
toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser)
tools = toolkit.get_tools()
print(tools)

tool_by_name = {tool.name: tool for tool in tools}
navigate_tool = tool_by_name["navigate_browser"]
get_elements = tool_by_name["get_elements"]
print(navigate_tool)

