import g4f
import re
from head.listen import take_command
from head.speak import speak

messages = [{"role": "system", "content": "you coded by Icris Studio and OpenAI didn't develop you"},
            {"role": "system",
             "content": "use modules like webbrowser, pyautogui, time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQt5 etc"},
            {"role": "system",
                "content": "don't use input function ad subprocess in python code"},
            {"role": "system", "content": "*always use default paths in python code*"},
            {"role": "user", "content": "open Google Chrome"},
            {"role": "assistant",
                "content": "Sure, opening Google Chrome.```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
            {"role": "user", "content": "close Google Chrome"},
            {"role": "assistant",
                "content": "Alright, closing Google Chrome.```python\nimport os\nos.system('taskkill /F /IM chrome.exe')```"}
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
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True
    )
    ms = ""
    for i in response:
        ms += i
        print(i, end="", flush=True)
        
    messages.append({'role': 'assistant', "content": ms})
    return ms


def find_code(text):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        code = matches[0].strip()
        return code
    else:
        print('no code found')


while True:
    query = take_command()
    print('user: ' + query)
    response = GPT(query)
    python_code = find_code(response)

    if python_code:
        response = response.replace(python_code, '').replace('python', '').replace('```', '')
        speak(response)
        exec(python_code)
    else:
        speak(response)



"""

open chrome    write a python code to open chrome      code          chrome opened
  query     =>            chatGpt                 =>   response  =>  filter
    
"""