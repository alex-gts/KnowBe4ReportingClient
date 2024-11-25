# KnowBe4Client Python Library

## Overview
The `KnowBe4Client` library provides a Python interface to interact with the KnowBe4 API, enabling users to easily access and manage their KnowBe4 account data. This includes retrieving user and group information, phishing campaign details, risk score histories, and more.

## Installation
To install the library, ensure you have Python installed on your system. You can then download the library files and include them in your project directory.

Alternatively, if the library is hosted on a package repository like PyPI, install it using pip:

`pip install KnowBe4Client`


## Usage
First, import the `KnowBe4Client` class from the library. Initialize the client with your API key and base URL. Then, call the methods provided by the client to interact with the KnowBe4 API.

Each method in the KnowBe4Client class corresponds to an endpoint in the KnowBe4 API, and exceptions are raised for error scenarios.

Example:
```python
from KnowBe4Client import KnowBe4Client

api_key = "your_api_key_here"
region = "us"  # Change based on your server location

# Get all users
users = client.get_all_users()
print(users)

# Get specific user
user = client.get_specific_user(user_id=12345)
print(user)

client = KnowBe4Client(api_key, region)

# Example: Get Account and Subscription Data (Section: Get Account and Subscription Data)
# No additional parameters required.
account_data = client.get_account_and_subscription_data()
print(account_data)  # Outputs account data including subscription level, number of seats, risk score history, etc.

# Example: Get Specific User (Section: Get a Specific User)
# Input: User ID (integer)
specific_user = client.get_specific_user(user_id=12345)
print(specific_user)  # Outputs data for the specified user.

# Example: Get Users in Group (Section: Get a List of Users in a Specific Group)
# Input: Group ID (integer)
users_in_group = client.get_users_in_group(group_id=67890)
print(users_in_group)  # Outputs a list of users in the specified group.

# Example: Get User Risk Score History (Section: Get a Specific User's Risk Score History)
# Input: User ID (integer), Full history (boolean, optional)
user_risk_score = client.get_user_risk_score_history(user_id=12345, full=True)
print(user_risk_score)  # Outputs risk score history for the specified user.

# Example: Get All Groups (Section: Get a List of All Groups)
# Optional parameters: status (string)
all_groups = client.get_all_groups(status='active')
print(all_groups)  # Outputs a list of all active groups.

# Example: Get Specific Group (Section: Get a Specific Group)
# Input: Group ID (integer)
specific_group = client.get_specific_group(group_id=67890)
print(specific_group)  # Outputs data for the specified group.

# Example: Get Group Risk Score History (Section: Get a Specific Group's Risk Score History)
# Input: Group ID (integer), Full history (boolean, optional)
group_risk_score = client.get_group_risk_score_history(group_id=67890, full=True)
print(group_risk_score)  # Outputs risk score history for the specified group.

# Example: Get Specific Phishing Campaign (Section: Get a Specific Phishing Campaign)
# Input: Campaign ID (integer)
phishing_campaign = client.get_specific_phishing_campaign(campaign_id=123)
print(phishing_campaign)  # Outputs data for the specified phishing campaign.

# Example: Get All Phishing Security Tests (Section: Get All Phishing Security Tests)
# No additional parameters required.
all_psts = client.get_all_phishing_security_tests()
print(all_psts)  # Outputs a list of all phishing security tests.

# Example: Get PSTs from Specific Campaign (Section: Get All PSTs From a Specific Campaign)
# Input: Campaign ID (integer)
psts_from_campaign = client.get_psts_from_specific_campaign(campaign_id=123)
print(psts_from_campaign)  # Outputs phishing security tests from the specified campaign.

```


