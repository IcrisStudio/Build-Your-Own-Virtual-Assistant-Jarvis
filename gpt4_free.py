import g4f

messages = [
    {'role': 'system', "content": "you are not a bing and not been developed by microsoft and your name is jarvis and you are dveloped by icris studio"},
    {'role': 'system', "content": "you are coded in python language by icris studio."}
]


def GPT(*args):
    
    global messages
    assert args!=()
    
    message = ''
    for i in args:
        message +=i
        
    messages.append({'role': 'user', "content": message})
    
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.Bing,
        messages=messages,
        stream=True
    )
    ms = ""
    for i in response:
        ms += i
        print(i, end="", flush=True)
        
    messages.append({'role': 'assistant', "content": ms})
    return ms

GPT('who are you')
