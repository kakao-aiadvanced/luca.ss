from openai import OpenAI

api_key = ""

history_teacher_system_prompt = """
You're a history enthusiast with a passion for bringing the past to life through storytelling and analysis. Your expertise lies in crafting engaging narratives that captivate your audience and make historical events feel relevant and relatable.
Your task is to provide a detailed explanation of the events leading up to and during the French Revolution. Incorporate key figures, crucial turning points, social dynamics, and the aftermath of this influential period in French history.
Remember to highlight the economic hardships, social inequalities, political unrest, and ideological conflicts that fueled the Revolution. Also, emphasize the impact of the Revolution on France and its lasting effects on the world stage.
For example, you would narrate how the French Revolution started with the financial crisis, escalating tensions between the estates, and the storming of the Bastille, ultimately leading to the rise of Robespierre and the Reign of Terror.
"""

question = "what is the Newton’s law? How did World War I end?"


openai_client = OpenAI(api_key=api_key)
response = openai_client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": history_teacher_system_prompt},
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
    {"role": "system", "content": history_teacher_system_prompt},
    {"role": "user", "content": question}
  ]
)

print("## llama3 - ollama")
print(response.choices[0].message.content)
print("\n\n")