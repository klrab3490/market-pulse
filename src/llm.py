import json
import os
from google import genai
from google.genai import types


# Create the client (this is where the API key is used)
client = genai.Client(api_key=os.getenv("LLM_API"))

# Define the generation configuration
# Adjust the thinking budget as needed; 0 means no thinking time
generation_config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0)
)

def format_prompt(ticker, momentum, news):
    news_formatted = "\n".join(
        [f"- {item['title']}: {item['description']}" for item in news]
    )
    return f"""
Given the following signals for the stock {ticker}, determine the market pulse and explain.

Momentum:
Returns: {momentum['returns']}
Score: {momentum['score']}

News:
{news_formatted}

Respond in strict JSON format:
{{
  "pulse": "bullish" | "bearish" | "neutral",
  "llm_explanation": "short explanation based on momentum and news"
}}
    """.strip()

async def get_market_pulse(ticker, momentum, news):
    prompt = format_prompt(ticker, momentum, news)

    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=generation_config,
    )

    text = response.text.strip()
    # print("Gemini Raw Output:", text)

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        import re
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            result = json.loads(match.group(0))
        else:
            raise ValueError("Could not extract JSON from LLM response")

    # print("Parsed JSON Result:", result)
    return result["pulse"], result["llm_explanation"]
