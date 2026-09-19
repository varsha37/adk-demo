from google.adk.agents import Agent

root_agent = Agent(
    name = "my_first_agent",
    model = "gemini-2.0-flash",
    description = "This is my first agent created using the ADK.",
    instructions = """
    You are a helpful assistant that can answer questions and provide information.
    """,)