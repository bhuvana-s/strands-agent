from strands import Agent
from strands.models import BedrockModel
from strands_tools import calculator, file_read

# Create an agent with Amazon Nova model and tools
model = BedrockModel(
    model_id="amazon.nova-micro-v1:0", 
    region="us-east-1"
)
agent = Agent(model=model, tools=[calculator, file_read])

# Ask the agent to show current directory contents
print("Asking: List the files in the current working directory")
try:
    response = agent("List the files in the current working directory using the file_read tool")
    print(f"Response: {response}")
except Exception as e:
    print(f"Error: {e}")
    print("The agent worked but may have hit a token limit or tool execution issue.")
