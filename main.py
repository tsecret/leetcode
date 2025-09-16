from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import os
import sys
import requests

transport = AIOHTTPTransport(url="https://leetcode.com/graphql/")
client = Client(transport=transport)

if len(sys.argv) < 2:
  print("Question slug is required")
  sys.exit(1)

parsedSlug = sys.argv[1]

def download():
  if os.path.exists(f'./problems/{parsedSlug}'):
    print(f'Question {parsedSlug} already exists')
    return

  query = gql(
      """
      query ($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            boundTopicId
            title
            titleSlug
            content
            translatedTitle
            translatedContent
            isPaidOnly
            difficulty
            likes
            dislikes
            isLiked
            similarQuestions
            exampleTestcases
            contributors {
                username
                profileUrl
                avatarUrl
            }
            topicTags {
                name
                slug
                translatedName
            }
            companyTagStats
            codeSnippets {
                lang
                langSlug
                code
            }
            stats
            hints
            solution {
                id
                canSeeDetail
                paidOnly
                hasVideoSolution
                paidOnlyVideo
            }
            status
            sampleTestCase
            metaData
            judgerAvailable
            judgeType
            mysqlSchemas
            enableRunCode
            enableTestMode
            enableDebugger
            envInfo
            libraryUrl
            adminUrl
            challengeQuestion {
                id
                date
                incompleteChallengeCount
                streakCount
                type
            }
            note
        }
    }
  """
  )
  query.variable_values = { "titleSlug": parsedSlug }

  result = client.execute(query)

  question = result['question']

  slug = question['titleSlug']

  os.makedirs(f'./problems/{slug}', exist_ok=True)

  # Solution

  solution = f"""
# URL: https://leetcode.com/problems/{slug}
# topics: {', '.join([tag['slug'] for tag in question['topicTags']])}

"""

  for codeSample in question['codeSnippets']:
    if codeSample['langSlug'] == 'python3':
      with open(f'./problems/{slug}/solution.py', "w") as f:
        f.write(solution + codeSample['code'])
      break

  # Tests
  sampleTestCaseN = len(question['sampleTestCase'].split('\n'))
  testCases = question['exampleTestcases'].split('\n')
  for i in range(0, len(testCases), sampleTestCaseN):
    print(testCases[i])


def downloadTestCases(slug: str):
  data = requests.get(f"https://datasets-server.huggingface.co/filter?dataset=newfacade/LeetCodeDataset&config=default&split=train&where=%22task_id%22%20%3D%20'{slug}'&length=10").json()
  question = data['rows'][0]['row']
  tests = 'from solution import Solution\n\n'
  tests += question['test']
  tests += '\n\n'
  tests += f'check({question['entry_point']})'

  with open(f'./problems/{slug}/test.py', "w") as f:
    f.write(tests)



downloadTestCases(parsedSlug)
