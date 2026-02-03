# Step1: Virtual Environment
# python3 -m venv .venv
#activate the venv
#.\.venv\Scripts\activate.bat
## if not vrutaul env seen - run the below for admin access 
# Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

## Import Ollama
from langchain_ollama import ChatOllama

llm = ChatOllama(model = "llama3")
prompt = " any prompt"
result = llm.invoke(prompt) #-- will invoke the llm and havet he result sored.
print(result)


## interactive prompts
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

while True:
    prompt = input("Enter your prompt (or 'quit' to exit): ")
    if prompt.lower() == "quit":
        break
    result = llm.invoke(prompt)
    print("\nResponse:\n", result, "\n")
