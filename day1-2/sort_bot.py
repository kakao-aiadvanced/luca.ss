from openai import OpenAI

api_key = ""

sort_system_prompt = """
You are an expert at sorting integers. 

Ascending sorting of integers means arranging them in order, starting with the smallest integer and ending with the largest integer.
Find the smallest number. For lists, you have to traverse the list to find the smallest number.
Move that number to the extreme left (or beginning) of the list.
Then find the next smallest number and repeat the above process.
This process is repeated until all elements in the list are sorted.
This will sort the numbers from smallest to largest.
However, if the same number appears more than once in the list to be sorted, the numbers are displayed as duplicates, and the order can follow a stable sorting method that maintains the original order or be positioned regardless of the original order.

<example>
question = [257, 420, 41, 527, 867, 685, 830, 433]
answer = [41, 257, 420, 433, 527, 685, 830, 867]
------------------------------
question = [400, 471, 923, 306, 222, 719, 209, 931, 459, 953, 225, 532, 90]
answer = [90, 209, 222, 225, 306, 400, 459, 471, 532, 719, 923, 931, 953]
------------------------------
question = [883, 853, 627, 761, 694, 712]
answer = [627, 694, 712, 761, 853, 883]
------------------------------
question = [218, 24, 294, 477, 224, 973, 282, 401]
answer = [24, 218, 224, 282, 294, 401, 477, 973]
------------------------------
question = [797, 478, 772, 924, 638, 396, 846, 125, 207, 245, 647, 809]
answer = [125, 207, 245, 396, 478, 638, 647, 772, 797, 809, 846, 924]
</example>

let's think about step by step.
If you answer this wrong, you will be in big trouble, so think carefully before answering.
"""

question = """
question = [42, 74, 5679, 34, 6, 6, 4567, 5, 6, 9, 278, 9, 767, 54, 883]
answer = 
"""


openai_client = OpenAI(api_key=api_key)
response = openai_client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": sort_system_prompt},
    {"role": "user", "content": question}
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
    {"role": "system", "content": sort_system_prompt},
    {"role": "user", "content": question}
  ]
)

print("## llama3 - ollama")
print(response.choices[0].message.content)
print("\n\n")


response = llama3_client.chat.completions.create(
  model="phi3",
  messages=[
    {"role": "system", "content": sort_system_prompt},
    {"role": "user", "content": question}
  ]
)

print("## phi3 - ollama")
print(response.choices[0].message.content)
print("\n\n")