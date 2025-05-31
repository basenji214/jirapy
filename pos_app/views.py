from django.shortcuts import render
from .jira_utils import test_connection

# Create your views here.

def jira_dashboard(request):
    # Test connection when loading the dashboard
    connection_status = test_connection()
    context = {
        'connection_status': connection_status,
    }
    return render(request,'pos_app/dashboard.html',context)


def search_issues(request):
    from .jira_utils import get_jira_connection
    issues = []
    if request.method == 'POST':
        jql = request.POST.get('jql','')n b 
        if jql:
            jira = get_jira_connection()
            issues = jira.jql(jql)
    context = {
        'issues': issues,
    }
    return render(request, 'pos_app/search.html', context)