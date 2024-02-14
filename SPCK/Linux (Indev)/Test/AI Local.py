import ollama

stream = ollama.chat(
    model='phi',
    messages=[

      {'role': 'system', 'content': "You are a helpful A.I. Your name is Eclahtee. Respond shortestly and only answer the main problem. Do not taking about \"Let's imagine that there are four different types of artificial intelligence\""},
      {'role': 'user', 'content': 'Hello'}
      
      ],
    stream=True,
)

for chunk in stream: print(chunk['message']['content'], end='', flush=True)