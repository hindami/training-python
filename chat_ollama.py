import asyncio
import httpx

API_URL = "http://localhost:11434/v1/chat/completions"

payload = {
    "model": "qwen3:1.7b",
    "messages": [{"role": "user", "content": "Do you know about hindami muhammad?"}],
}


async def request():
    timeout = httpx.Timeout(160.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(API_URL, json=payload)
        data = response.json()
        print(data["choices"][0]["message"]["content"])


asyncio.run(request())
