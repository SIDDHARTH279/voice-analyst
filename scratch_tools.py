from dotenv import load_dotenv
from groq import Groq
from src.tools.finance import get_financials
import os 
import json


load_dotenv()
client = Groq()

tools = [
    {
        'type': 'function',
        'function': {
            'name': 'get_financials',
            'description': 'Get key financial metrics (price, P/E, growth, margins) for a listed company by its stock ticker. Indian NSE stocks end with .NS',
            'parameters': {
                'type': 'object',
                'properties': {
                    'ticker': {
                        'type': 'string',
                        'description': 'stock ticker, e.g. TCS.NS'
                    }
                },
                'required': ['ticker']
            }
        }
    }
]

messages = [{'role': 'user', 'content': "what's TCS's P/E ratio?"}]

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    tools=tools,
)


msg = response.choices[0].message
messages.append(msg)  # the model must see its own tool request

for tool_call in msg.tool_calls:
    args = json.loads(tool_call.function.arguments)
    result = get_financials(**args)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result),
    })

final = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
)
print(final.choices[0].message.content)