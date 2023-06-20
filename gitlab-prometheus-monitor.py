from gitlab import Gitlab
from prometheus_client import start_http_server, Gauge
from datetime import datetime, timedelta
import time

# Initialize a GitLab object with your GitLab instance URL and a private token
gl = Gitlab('https://gitlab.com', private_token='your_private_token')

# Specify the project ID that you want to monitor
project_id = 123

# Specify the time window in which you want to monitor events
start_time = datetime.now() - timedelta(minutes=5)  # 5 minutes ago
end_time = datetime.now()  # Now

# Initialize Prometheus metrics
mr_count = Gauge('merge_requests_count', 'Total number of merge requests')
issue_count = Gauge('issue_count', 'Total number of issues')


# Define a function to update the metrics
def update_metrics():
    # Get a list of all merge requests in the specified time window
    merge_requests = gl.project_merge_requests.list(project_id, created_after=start_time, created_before=end_time)

    # Get a list of all issues in the specified time window
    issues = gl.project_issues.list(project_id, created_after=start_time, created_before=end_time)

    # Set the value of the Prometheus metrics
    mr_count.set(len(merge_requests))
    issue_count.set(len(issues))

# Start the Prometheus HTTP server on port 8000
start_http_server(8000)

# Loop forever and update the metrics every 10 seconds
while True:
    update_metrics()
    time.sleep(10)
