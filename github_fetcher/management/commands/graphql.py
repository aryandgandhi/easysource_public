import requests

def fetch_good_first_issues_graphql():

    url = 'https://api.github.com/graphql'
    headers = {'Authorization': 'Bearer your token'}

    query = """
    query {
      search(type: ISSUE, query: "label:good-first-issue state:open", first: 100) {
        nodes {
          ... on Issue {
            title
            url
            bodyText
            repository {
              name
              url
              description
            }
          }
        }
      }
    }
    """

    response = requests.post(url, json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {query}")


issues_data = fetch_good_first_issues_graphql()
print(issues_data)
