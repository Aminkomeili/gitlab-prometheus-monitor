# GitLab Prometheus Monitor

This is a Python program that collects GitLab activities using the GitLab API and generates Prometheus metrics using the prometheus_client library.
## Prerequisites

To use this program, you will need:

1. Python 3.6 or later
2. gitlab and prometheus_client Python packages

To install the required packages, run:

`pip install -r requirements.txt`

## Usage

To use this program, you will need:

1. A GitLab instance with an access token that has API access.
2. The ID of the project that you want to monitor.

To run the program, execute the following command:


`python gitlab_prometheus_monitor.py <gitlab_url> <access_token> <project_id>`

For example:

`python gitlab_prometheus_monitor.py https://gitlab.com my_access_token 123`

This will start the Prometheus HTTP server on port 8000 and collect GitLab activities every 10 seconds.

To view the Prometheus metrics, open http://localhost:8000 in your web browser.
## Metrics

This program generates the following Prometheus metrics:

1. merge_requests_count: Total number of merge requests in the specified time window.
2. issue_count: Total number of issues in the specified time window.

## License

This program is licensed under the MIT License. See the LICENSE file for details.
