from strands import Agent
from strands.models import BedrockModel
from strands_tools import calculator

# Create an agent with Amazon Nova model and calculator tool
model = BedrockModel(
    model_id="amazon.nova-micro-v1:0", 
    region="us-east-1"
)
agent = Agent(model=model, tools=[calculator])

# Ask the agent to do a calculation
print("Asking: What is 25 * 4 + 10?")
try:
    response = agent("What is 25 * 4 + 10? Use the calculator tool to compute this.")
    print(f"Response: {response}")
except Exception as e:
    print(f"Error: {e}")
    print("The agent worked but may have hit a token limit or tool execution issue.")
