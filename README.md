# Strands AgentCore Setup Guide

This repository contains AI agents built using the Strands framework and AWS Bedrock. Follow this guide to set up your environment and run the agents successfully.

## Prerequisites

- macOS or Linux system
- AWS account with Bedrock access
- AWS CLI configured with valid credentials
- Internet connection for downloading dependencies

## Quick Start

### 1. Install Python 3.10+

The `strands-agents` package requires Python 3.10 or higher. If you don't have it installed:

```bash
# Install pyenv (Python version manager)
curl https://pyenv.run | bash

# Add pyenv to your shell (add these lines to ~/.bashrc or ~/.zshrc)
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Restart your shell or source your profile
source ~/.bashrc  # or ~/.zshrc

# Install Python 3.10
pyenv install 3.10.12
pyenv local 3.10.12
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment with Python 3.10
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install strands-agents boto3 feedparser
```

### 3. Configure AWS

Ensure your AWS credentials are configured and you're using the correct region:

```bash
# Check your AWS configuration
aws configure list

# Set the region to us-east-1 (required for this project)
export AWS_DEFAULT_REGION=us-east-1
```

**Why us-east-1?** This project is configured to use AWS Bedrock models in the `us-east-1` region because:
- The deployment configuration (`.bedrock_agentcore.yaml`) specifies us-east-1
- Many AWS Bedrock models have the best availability in us-east-1
- The project's AWS resources and IAM roles are set up in this region

## Running the Agents

### Option 1: Working Agent (Recommended)

This agent uses Amazon Titan model which is immediately available:

```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Set AWS region
export AWS_DEFAULT_REGION=us-east-1

# Run the working agent
python working_agent.py
```

**Expected Output:**
```
Asking: What is AWS?
Response: AWS, also known as Amazon Web Services, is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs...
```

### Option 2: Original Simple Agent

This agent requires access to third-party models (like Claude):

```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Set AWS region
export AWS_DEFAULT_REGION=us-east-1

# Run the original agent
python ./01_simple_agent/agent.py
```

**Note:** If you get an "AccessDeniedException", you need to request access to Claude models in the AWS Bedrock Console.

## Troubleshooting

### Python Version Issues
```bash
# Check Python version
python --version

# Should show Python 3.10.x or higher
# If not, ensure pyenv is properly configured and activated
```

### AWS Access Issues
```bash
# Test AWS connectivity
aws sts get-caller-identity

# List available Bedrock models
aws bedrock list-foundation-models --region us-east-1
```

### Model Access Issues

If you get "AccessDeniedException" errors:

1. **Go to AWS Bedrock Console** (https://console.aws.amazon.com/bedrock/)
2. **Navigate to "Model access"** in the left sidebar
3. **Request access** to the models you want to use (e.g., Claude models)
4. **Wait for approval** (usually takes a few minutes)

### Common Error Solutions

**Error: `ModuleNotFoundError: No module named 'strands'`**
- Solution: Activate virtual environment and install strands-agents

**Error: `ValidationException: The provided model identifier is invalid`**
- Solution: Use a valid model ID like `amazon.titan-text-express-v1`

**Error: `AccessDeniedException: You don't have access to the model`**
- Solution: Request model access in AWS Bedrock Console or use Amazon Titan models

**Error: `MaxTokensReachedException`**
- Solution: This is normal behavior; the agent completed its response but hit token limits

## Available Models

### Immediately Available (Amazon Models)
- `amazon.titan-text-express-v1` - Fast, cost-effective text generation
- `amazon.titan-text-lite-v1` - Lightweight text model
- `amazon.nova-micro-v1:0` - Latest Amazon model

### Requires Access Request
- `anthropic.claude-3-haiku-20240307-v1:0` - Fast, accurate responses
- `anthropic.claude-3-sonnet-20240229-v1:0` - Balanced performance
- `meta.llama3-8b-instruct-v1:0` - Open source model

## Project Structure

```
strands-agentcore/
├── README.md                    # This file
├── requirements 2.txt           # Python dependencies
├── working_agent.py            # Agent with Titan model (works immediately)
├── test_agent.py              # Test agent with Claude model
├── venv/                      # Virtual environment
├── 01_simple_agent/
│   ├── agent.py              # Original simple agent
│   └── agent_with_tool.py    # Agent with tools
├── deploy_agent/
│   └── .bedrock_agentcore.yaml # AWS deployment configuration
└── aws_news_digest_agent/     # News digest agent example
```

## Next Steps

1. **Experiment with different models** by modifying the `model_id` in your agent scripts
2. **Add tools and capabilities** by exploring the `strands-agents-tools` package
3. **Deploy to AWS** using the Bedrock AgentCore configuration
4. **Build custom agents** for your specific use cases

## Support

- **Strands Documentation**: https://strandsagents.com/
- **AWS Bedrock Documentation**: https://docs.aws.amazon.com/bedrock/
- **AWS Bedrock Model Access**: https://console.aws.amazon.com/bedrock/

## Environment Variables

For convenience, you can set these environment variables in your shell profile:

```bash
# Add to ~/.bashrc or ~/.zshrc
export AWS_DEFAULT_REGION=us-east-1
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Happy coding with Strands AgentCore! 🚀
