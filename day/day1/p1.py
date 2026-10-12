#variables
temperature = 0.7 #float
max_tokens = 1024 #int
is_streaming = False #boolean
content_box = None #None

#Type hints
model_name:str = "gemimi-2.0-flash"
temperature: float = 0.7 #float
max_tokens:int = 1024 #int
is_streaming:bool = False #boolean
content_box:str|None = None #None
print(type(model_name))

#Strings:immtuable | string formation
#Old version
name="LLM"
score =97.4
print("Hello %s"%name)
print("score %.1f"%score)

#f-strings(py 3.6+)
print(f"Hello{name}")
print(f"Score:{score:.1f}")

# Expressions inside f-strings
word_limit = 200
print(f"{'Over'if word_limit > 150 else'under'}limit")

data = {"Topic":"RAG"}
print(f"Topic:{data['Topic']}")
# format specifier
pi = 3.14159265
print(f"pi:{pi:.2f}")

#debugging =
temp = 0.7
print(f"{temp=}")

# multi line f-strings formatting
user_input = " what is langchain?"
context_text = "langchain is a framework\"for building LLM apps"
system_prompt = f""" 
you are a helpful AI tutor.
context provided:{context_text}
student question:{user_input}
Instructins:
- answer based only on the context above
- if the answer is not in the context,say "I don't know
- keep your answers under 3 sentences
""".strip()
print(system_prompt)

# lists: ordered,mutable,heterogenous sequence
# in GEN AI: chat history,chunks of retreived documents
# token sequences
chat_history: list [dict]=[
    {"role":"user","content":"what is an LLM"},
    {"role":"assistant","content":"a LLM ia a neural n/w trained on vast amounts of text."},
]
#access
first_msg =  chat_history[0]
print(first_msg)
print(chat_history[-1]["content"])

#modify
chat_history.append({"role":"user","content":"what is a RAG?"})
print(chat_history)
chat_history.pop()
print(chat_history)

#iterate
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['content']}")


# list of documents chunks
chunks:list[str] =[
    "RAG stands for retereival augmneted generation",
    "it combines a retreiver with a generator",
]
# filter chunks based on length
valid_chunks = [c for c in chunks if len(c.split())>=6]
print(valid_chunks)