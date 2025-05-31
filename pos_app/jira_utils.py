from atlassian import Jira
from django.conf import settings

def get_jira_connection():
    """
    Returns a Jira connection instance
    """
    jira = Jira(
        url = settings.JIRA_SERVER,
        username = settings.JIRA_USERNAME,
        password = settings.JIRA_API_TOKEN,
        cloud = True    # Set to False if using self-hosted Jira
    )
    return jira


def test_connection():
    """
    Test the Jira connection and return basic info
    """
    try:
        jira = get_jira_connection()
        user = jira.myself()
        server_info = jira.get_server_info()
        return {
            'success': True,
            'user': user,
            'server_info': server_info
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
    

def create_issue(project_key, summary, description, issue_type='Task'):
    jira = get_jira_connection()
    issue = jira.issue_create(
        fields={
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }
    )
    return issue

def get_issue(issue_key):
    jira = get_jira_connection()
    return jira.issue(issue_key)

def update_issue(issue_key, updates):
    jira = get_jira_connection()
    return jira.issue_update(issue_key, updates)

def add_comment(issue_key, comment):
    jira = get_jira_connection()
    return jira.issue_add_comment(issue_key, comment)
