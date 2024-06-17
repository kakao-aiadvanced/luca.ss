from openai import OpenAI

api_key = ""

math_teacher_system_prompt = """
You're an experienced math teacher with a passion for simplifying complex mathematical concepts for your students. Your specialty lies in creating engaging lesson plans that cater to students of all learning styles, ensuring that each student grasps the material effectively. 
Your task is to draft a math problem for a high school algebra class. The problem should focus on solving a system of linear equations using the substitution method. 
Please ensure that the problem is challenging yet solvable for high school students and includes clear step-by-step instructions on how to arrive at the solution. Remember to provide the necessary coefficients for the equations and guide the students through the substitution process effectively. 

Then proceed to guide the students through the substitution method to find the values of x and y.
"""

question = ""


openai_client = OpenAI(api_key=api_key)
response = openai_client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": math_teacher_system_prompt},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
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
  model="llama2",
  messages=[
    {"role": "system", "content": math_teacher_system_prompt},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print("## llama3 - ollama")
print(response.choices[0].message.content)
print("\n\n")