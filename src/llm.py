import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GROQ_API_KEY')
client = Groq(api_key=API_KEY)

def extractSolutionCode(solution):
  response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[

        {
            "role": "system",
            "content": """
              You are a coding expert specializing in reading LeetCode solution and extracting the solution code.
            """
        },
        {
            "role": "user",
            "content": f"""
              Here is the solution article for one of the LeetCode problems. Please extract the most optimal python solution as a code snippet that I can copy-paste to my file.

              {solution['content']}

              Important:
              - Do not inclide if __name__ == "__main__".

            """,
        }
    ],
    response_format = {
      "type": "json_schema",
      "json_schema": {
        "name": "test_cases",
        "schema": {
          "type": "object",
          "properties": {
            "solution_code": {"type": "string"},
          },
        },
        "required": ['solution_code']
      }
    }
    )

  return json.loads(response.choices[0].message.content)

def generateTestCases(problem, solution_code):
  starting_code = None

  for code in problem['codeSnippets']:
    if code['langSlug'] == 'python3':
      starting_code = code['code']

  assert starting_code, 'Starting Code for python3 not found'

  response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[

        {
            "role": "system",
            "content": """
              You are a coding expert specializing in generating comprehensive test cases for LeetCode problems.

              CRITICAL INSTRUCTIONS:
              1. Focus on edge cases, boundary conditions, and typical scenarios
              2. Ensure test cases cover the problem constraints
              3. Generate at least 20 diverse test cases
              4. Use descriptive test case names that explain what scenario is being tested
            """
        },
        {
            "role": "user",
            "content": f"""
              Given the following LeetCode problem with the starting code:

              {starting_code}

              Additionally, here is a code solution for this problem:

              {solution_code}

              Generate comprehensive Python unittest test cases. Then run the code to validate the test cases using the solution code above.

              Also, consider the constraints. The test cases should not test for invalid input or error handler. Assume the input is always valid.
              If the problem contains string inputs, make sure the meaning of input string makes sense (For example in roman to integer problem)

              The file with solution code will be name "solution_{problem['titleSlug'].replace('-', '_')}.py"
              Do not inclide if __name__ == "__main__"
            """,
        }
    ],
    response_format = {
      "type": "json_schema",
      "json_schema": {
        "name": "test_cases",
        "schema": {
          "type": "object",
          "properties": {
            "test_cases": {"type": "string"},
            "comments": {"type": "string"},
            "solution_code_used": {"type": "string"},
          },
        },
        "required": ["test_cases", 'solution_code_used']
      }
    }
    )

  if response.choices[0].message.executed_tools:
    print(response.choices[0].message.executed_tools[0])

  return json.loads(response.choices[0].message.content)
