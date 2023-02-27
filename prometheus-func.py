# Initialize Prometheus metrics
mr_count = Gauge('merge_requests_count', 'Total number of merge requests')
issue_count = Gauge('issue_count', 'Total number of issues')
file_count = Counter('file_count', 'Total number of files in the project')

# Define a function to update the metrics
def update_metrics():
    # Get a list of all merge requests in the specified time window
    merge_requests = gl.project_merge_requests.list(project_id, created_after=start_time, created_before=end_time)

    # Get a list of all issues in the specified time window
    issues = gl.project_issues.list(project_id, created_after=start_time, created_before=end_time)

    # Get a list of all files in the project
    files = gl.project_files.list(project_id)

    # Set the value of the Prometheus metrics
    mr_count.set(len(merge_requests))
    issue_count.set(len(issues))
    file_count.inc(len(files))

# Start the Prometheus HTTP server on port 8000
start_http_server(8000)

# Loop forever and update the metrics every 10 seconds
while True:
    update_metrics()
    time.sleep(10)
