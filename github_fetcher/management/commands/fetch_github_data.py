import requests
from django.core.management.base import BaseCommand
from github_fetcher.models import Project, Issue
from github_fetcher.bard import get_bard_summary, get_bard_summary_issue,get_bard_difficulty
import time

class Command(BaseCommand):
    help = 'Fetch data from the GitHub API and update the database'

    def handle(self, *args, **options):
                  
        headers = {'Authorization': 'token your_token_goes_here'}
        names = [
    'gfi-bot', 
    'good-first-issues-bot', 
    'good-first-issue-finder', 
    'Good_First_Issue_Web_App', 
    'Issues-Hunt', 
    'spatie-good-first-issue-finder', 
    'good-first-issue', 
    'other-name-1', 
    'other-name-2'
]


        page = 1
        repo_count = 0
        while True:
            # Fetch the good-first-issues from the GitHub API
            issues_response = requests.get(
                'https://api.github.com/search/issues',
                headers=headers, 
                params={'q': 'label:good-first-issue state:open', 'per_page': 100, 'page': page}
            )

            issues_data = issues_response.json().get('items', [])

            if not issues_data or repo_count >= 10:
                break

            for issue_data in issues_data:
                # Fetch the repo details from the GitHub API
                repo_response = requests.get(issue_data['repository_url'], headers=headers)
                repo_data = repo_response.json()
        

                # Fetch the bard summary for this project
                time.sleep(2)
                bard_summary_project = get_bard_summary(repo_data['html_url'])

                if repo_data['name'] not in names:      # Create or update the Project object
                    project, created = Project.objects.update_or_create(
                        github_url=repo_data['html_url'],
                        defaults={
                            'name': repo_data['name'],
                            'description': repo_data['description'],
                            'summary': bard_summary_project,  # save the bard summary for project
                        }
                    )
                    print(f'Saved project {project.name}')


                    # Fetch the bard summary for this issue
                    time.sleep(2)
                    bard_summary_issue = get_bard_summary_issue(issue_data['repository_url'], issue_data['body'])
                    bard_difficulty = get_bard_difficulty(issue_data['body'])
                    print(issue_data['repository_url'])
                    print(bard_difficulty)

                    # Create or update the Issue object
                    Issue.objects.update_or_create(
                        github_url=issue_data['html_url'],
                        defaults={
                            'project': project,
                            'title': issue_data['title'],
                            'description': issue_data['body'],
                            'bard_summary': bard_summary_issue,  # save the bard summary for issue
                            'difficulty': bard_difficulty,
                        }
                    )
          
                    print(f'Saved issue {issue_data["title"]}')


                    repo_count += 1
                    if repo_count >= 5:
                        break

            page += 1

        self.stdout.write(self.style.SUCCESS('Successfully updated data from GitHub API'))
