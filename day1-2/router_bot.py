from openai import OpenAI

api_key = ""

router_system_prompt = """
You are the expert who judges which expert will be better at answering the question depending on what kind of question it is.
Here are some experts you may know:
    - history_teacher: Teacher with rich knowledge of history
    - math_teacher: Teacher with extensive knowledge of mathematics

Depending on the user's questions, select an expert who can better answer them.
There is only one correct answer, and if the question is ambiguous, indicate the score for each expert and choose the highest one.

Please respond only in json format, including only expert and description as keys.
"""

question1 = "what is the Newton’s law?"
question2 = "How did World War I end?"


openai_client = OpenAI(api_key=api_key)
response = openai_client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": router_system_prompt},
    {"role": "user", "content":question1}
  ]
)

print("## openai")
print(response.choices[0].message.content)
print("\n\n")






llama3_client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

response = llama3_client.chat.completions.create(
  model="llama3",
  messages=[
    {"role": "system", "content": router_system_prompt},
    {"role": "user", "content": question1}
  ]
)

print("## llama3 - ollama")
print(response.choices[0].message.content)
print("\n\n")


response = llama3_client.chat.completions.create(
  model="phi3",
  messages=[
    {"role": "system", "content": router_system_prompt},
    {"role": "user", "content": question1}
  ]
)

print("## phi3 - ollama")
print(response.choices[0].message.content)
print("\n\n")