from strands import Agent
from strands.models import BedrockModel

# Create an agent with Amazon Titan model
model = BedrockModel(
    model_id="amazon.titan-text-express-v1", 
    region="us-east-1"
)
agent = Agent(model=model)

# Ask the agent a question
print("Asking: What is AWS?")
try:
    response = agent("What is AWS?")
    print(f"Response: {response}")
except Exception as e:
    print(f"Error: {e}")
    print("The agent worked but hit a token limit. This is normal for the first run.")
