# Simple Agent Examples

This directory contains basic AI agent examples built using the Strands framework and AWS Bedrock. These examples demonstrate different agent configurations and capabilities.

## Prerequisites

Before running these agents, ensure you have completed the setup from the main project README:

- Python 3.10+ installed via pyenv
- Virtual environment activated (`source ../venv/bin/activate`)
- AWS credentials configured
- `strands-agents` package installed
- AWS region set to `us-east-1`

## Available Agents

### 1. agent.py (Recommended - Works Immediately)

**Description**: Basic agent using Amazon Titan model which is immediately available without access requests.

**Usage**:
```bash
# From the project root directory
source venv/bin/activate
export AWS_DEFAULT_REGION=us-east-1
python ./01_simple_agent/agent.py
```

**Expected Output**:
```
Asking: What is AWS?
Response: AWS, also known as Amazon Web Services, is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs...
```

**Model Used**: `amazon.titan-text-express-v1`

### 2. agent_calculator.py (Calculator Tool Example)

**Description**: Agent with calculator tool using Amazon Nova model for mathematical computations.

**Prerequisites**:
```bash
pip install strands-agents-tools
```

**Usage**:
```bash
# From the project root directory
source venv/bin/activate
export AWS_DEFAULT_REGION=us-east-1
python ./01_simple_agent/agent_calculator.py
```

**Expected Output**:
```
Asking: What is 25 * 4 + 10?
Response: The computation of the expression "25 * 4 + 10" yields the result of **110**.
```

**Model Used**: `amazon.nova-micro-v1:0`

### 3. agent_current_dir.py (File Operations Example)

**Description**: Agent with file_read and calculator tools for directory listing and file operations.

**Prerequisites**:
```bash
pip install strands-agents-tools
```

**Usage**:
```bash
# From the project root directory
source venv/bin/activate
export AWS_DEFAULT_REGION=us-east-1
python ./01_simple_agent/agent_current_dir.py
```

**Model Used**: `amazon.nova-micro-v1:0`

**Note**: This agent may hit token limits when listing large directories due to extensive output.

## Model Compatibility

### Immediately Available (Amazon Models)
- ✅ `amazon.titan-text-express-v1` - Text generation (no tools)
- ✅ `amazon.nova-micro-v1:0` - Text generation with tool support
- ✅ `amazon.nova-lite-v1:0` - Enhanced text generation with tools
- ✅ `amazon.nova-pro-v1:0` - Advanced text generation with tools

### Requires Access Request
- ⚠️ `anthropic.claude-3-haiku-20240307-v1:0` - Fast, accurate responses
- ⚠️ `anthropic.claude-3-sonnet-20240229-v1:0` - Balanced performance
- ⚠️ `meta.llama3-8b-instruct-v1:0` - Open source model

## Tool Support

### Available Tools (via strands-agents-tools)
- **calculator** - Mathematical computations and expressions
- **file_read** - File and directory operations
- **And many more** - Web scraping, API calls, data processing

### Tool Compatibility
- ❌ **Titan models** - Don't support tools in streaming mode
- ✅ **Nova models** - Full tool support
- ✅ **Claude models** - Full tool support (requires access)

## Troubleshooting

### Common Errors

**Error: `AccessDeniedException: You don't have access to the model`**
- **Solution**: Use Amazon models (Titan/Nova) or request access in AWS Bedrock Console

**Error: `ModuleNotFoundError: No module named 'strands_tools'`**
- **Solution**: `pip install strands-agents-tools`

**Error: `This model doesn't support tool use in streaming mode`**
- **Solution**: Use Nova models instead of Titan for tool-enabled agents

**Error: `Input Tokens Exceeded: Number of input tokens exceeds maximum length`**
- **Solution**: Normal for large outputs; try simpler queries or different models

**Error: `MaxTokensReachedException`**
- **Solution**: Normal behavior; agent completed response but hit token limits

### Model Access Setup

To request access to third-party models:

1. Go to [AWS Bedrock Console](https://console.aws.amazon.com/bedrock/)
2. Navigate to "Model access" in the left sidebar
3. Click "Request model access"
4. Select desired models (e.g., Claude 3 Haiku, Claude 3 Sonnet)
5. Submit request and wait for approval (usually a few minutes)

## File Descriptions

- **`agent.py`** - Basic agent with Amazon Titan model (text-only, no tools)
- **`agent_calculator.py`** - Agent with calculator tool using Nova model
- **`agent_current_dir.py`** - Agent with file operations and calculator tools
- **`README.md`** - This documentation file

## Creating Custom Agents

### Basic Text Agent
```python
from strands import Agent
from strands.models import BedrockModel

model = BedrockModel(
    model_id="amazon.titan-text-express-v1", 
    region="us-east-1"
)
agent = Agent(model=model)
response = agent("Your question here")
```

### Agent with Tools
```python
from strands import Agent
from strands.models import BedrockModel
from strands_tools import calculator, file_read

model = BedrockModel(
    model_id="amazon.nova-micro-v1:0", 
    region="us-east-1"
)
agent = Agent(model=model, tools=[calculator, file_read])
response = agent("Calculate 15 * 8 and list current directory")
```

## Next Steps

1. **Start with `agent.py`** to verify your basic setup
2. **Try `agent_calculator.py`** to test tool functionality
3. **Experiment with `agent_current_dir.py`** for file operations
4. **Create custom agents** by modifying these examples
5. **Request model access** for advanced models like Claude
6. **Explore more tools** in the strands-agents-tools package

## Support

- **Strands Documentation**: https://strandsagents.com/
- **AWS Bedrock Documentation**: https://docs.aws.amazon.com/bedrock/
- **AWS Bedrock Model Access**: https://console.aws.amazon.com/bedrock/

## Environment Setup Reminder

Always ensure these are set before running agents:

```bash
# Activate virtual environment
source ../venv/bin/activate

# Set AWS region
export AWS_DEFAULT_REGION=us-east-1

# Verify AWS credentials
aws sts get-caller-identity

# Install tools if needed
pip install strands-agents-tools
```
