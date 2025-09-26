from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from typing import List, Any

transport = AIOHTTPTransport(url="https://leetcode.com/graphql/")
client = Client(transport=transport)

def getListOfQuestions() -> List[Any]:
  query = gql(
      """
      query problemsetQuestionListV2(
          $filters: QuestionFilterInput
          $limit: Int
          $searchKeyword: String
          $skip: Int
          $sortBy: QuestionSortByInput
          $categorySlug: String
      ) {
          problemsetQuestionListV2(
              filters: $filters
              limit: $limit
              searchKeyword: $searchKeyword
              skip: $skip
              sortBy: $sortBy
              categorySlug: $categorySlug
          ) {
              questions {
                  id
                  titleSlug
                  title
                  translatedTitle
                  questionFrontendId
                  paidOnly
                  difficulty
                  topicTags {
                      name
                      slug
                      nameTranslated
                  }
                  status
                  isInMyFavorites
                  frequency
                  acRate
                  contestPoint
              }
              totalLength
              finishedLength
              hasMore
          }
      }
    """
  )
  query.variable_values = {
        "skip": 0,
        "limit": 100,
        "categorySlug": "all-code-essentials",
        "filters": {
            "filterCombineType": "ALL",
            "statusFilter": {
                "questionStatuses": [],
                "operator": "IS"
            },
            "difficultyFilter": {
                "difficulties": [
                    "EASY"
                ],
                "operator": "IS"
            },
            "languageFilter": {
                "languageSlugs": [
                    "python3"
                ],
                "operator": "IS"
            },
            "topicFilter": {
                "topicSlugs": [],
                "operator": "IS"
            },
            "acceptanceFilter": {},
            "frequencyFilter": {},
            "frontendIdFilter": {},
            "lastSubmittedFilter": {},
            "publishedFilter": {},
            "companyFilter": {
                "companySlugs": [],
                "operator": "IS"
            },
            "positionFilter": {
                "positionSlugs": [],
                "operator": "IS"
            },
            "contestPointFilter": {
                "contestPoints": [],
                "operator": "IS"
            },
            "premiumFilter": {
                "premiumStatus": [],
                "operator": "IS"
            }
        },
        "sortBy": {
            "sortField": "FRONTEND_ID",
            "sortOrder": "ASCENDING"
        }
    }

  res = client.execute(query)

  return res['problemsetQuestionListV2']['questions']

def getQuestionDetail(slug: str):
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
  query.variable_values = { "titleSlug": slug }
  res = client.execute(query)
  return res['question']

def getSolutions(slug: str) -> List[Any]:
  query = gql(
      """
      query ugcArticleSolutionArticles(
          $questionSlug: String!
          $orderBy: ArticleOrderByEnum
          $userInput: String
          $tagSlugs: [String!]
          $skip: Int
          $before: String
          $after: String
          $first: Int
          $last: Int
          $isMine: Boolean
      ) {
          ugcArticleSolutionArticles(
              questionSlug: $questionSlug
              orderBy: $orderBy
              userInput: $userInput
              tagSlugs: $tagSlugs
              skip: $skip
              first: $first
              before: $before
              after: $after
              last: $last
              isMine: $isMine
          ) {
              totalNum
              pageInfo {
                  hasNextPage
              }
              edges {
                  node {
                      ...ugcSolutionArticleFragment
                  }
              }
          }
      }

      fragment ugcSolutionArticleFragment on SolutionArticleNode {
          uuid
          title
          slug
          summary
          author {
              realName
              userAvatar
              userSlug
              userName
              nameColor
              certificationLevel
              activeBadge {
                  icon
                  displayName
              }
          }
          articleType
          thumbnail
          summary
          createdAt
          updatedAt
          status
          isLeetcode
          canSee
          canEdit
          isMyFavorite
          chargeType
          myReactionType
          topicId
          hitCount
          hasVideoArticle
          reactions {
              count
              reactionType
          }
          title
          slug
          tags {
              name
              slug
              tagType
          }
          topic {
              id
              topLevelCommentCount
          }
      }
    """
  )
  query.variable_values = {
      "questionSlug": slug,
      "skip": 0,
      "first": 15,
      "orderBy": "MOST_VOTES",
      "userInput": "",
      "tagSlugs": ["python3"]
  }

  res = client.execute(query)

  return [edge['node'] for edge in res['ugcArticleSolutionArticles']['edges']]

def getSolutionDetails(topicId: str):
  query = gql(
      """
        query ugcArticleSolutionArticle($articleId: ID, $topicId: ID) {
            ugcArticleSolutionArticle(articleId: $articleId, topicId: $topicId) {
                ...ugcSolutionArticleFragment
                content
                isSerialized
                isAuthorArticleReviewer
                scoreInfo {
                    scoreCoefficient
                }
                prev {
                    uuid
                    slug
                    topicId
                    title
                }
                next {
                    uuid
                    slug
                    topicId
                    title
                }
            }
        }

        fragment ugcSolutionArticleFragment on SolutionArticleNode {
            uuid
            title
            slug
            summary
            author {
                realName
                userAvatar
                userSlug
                userName
                nameColor
                certificationLevel
                activeBadge {
                    icon
                    displayName
                }
            }
            articleType
            thumbnail
            summary
            createdAt
            updatedAt
            status
            isLeetcode
            canSee
            canEdit
            isMyFavorite
            chargeType
            myReactionType
            topicId
            hitCount
            hasVideoArticle
            reactions {
                count
                reactionType
            }
            title
            slug
            tags {
                name
                slug
                tagType
            }
            topic {
                id
                topLevelCommentCount
            }
        }

    """
  )
  query.variable_values = { "topicId": topicId }
  res = client.execute(query)
  return res['ugcArticleSolutionArticle']
