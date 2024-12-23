import logging
import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)


from KnowBe4Client.auth import get_auth_header
from KnowBe4Client.utils import (
    handle_response,
    APIError,
)

BASE_URLS = {
    "US": "https://us.api.knowbe4.com",
    "EU": "https://eu.api.knowbe4.com",
    "CA": "https://ca.api.knowbe4.com",
    "UK": "https://uk.api.knowbe4.com",
    "DE": "https://de.api.knowbe4.com",
}

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("KnowBe4Client")


class KnowBe4Client:
    def __init__(self, api_key, region="US"):
        self.base_url = BASE_URLS.get(region)
        self.headers = get_auth_header(api_key)

    @retry(
        stop=stop_after_attempt(6),
        wait=wait_exponential(multiplier=1, min=2, max=32),
        retry=retry_if_exception_type((requests.exceptions.RequestException, APIError)),
        before_sleep=lambda retry_state: logger.warning(
            f"Retrying ({retry_state.attempt_number}/{retry_state.retry_object.stop.max_attempt_number-1})..."
        ),
        reraise=True,
    )
    def _get(self, endpoint, params=None):
        response = requests.get(
            f"{self.base_url}{endpoint}", headers=self.headers, params=params
        )

        return handle_response(response)

    def get_account_and_subscription_data(self, **params):
        try:
            return self._get("/v1/account", params=params)
        except APIError as e:
            print(f"Error getting account data: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_user_risk_score_history(self, user_id, full=False, **params):
        try:
            params = {**params, "full": "true"} if full else {}
            return self._get(f"/v1/users/{user_id}/risk_score_history", params=params)
        except APIError as e:
            print(f"Error getting user risk score history: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_all_groups(self, **params):
        try:
            return self._get("/v1/groups", params=params)
        except APIError as e:
            print(f"Error getting all groups: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_group(self, group_id, **params):
        try:
            return self._get(f"/v1/groups/{group_id}", params=params)
        except APIError as e:
            print(f"Error getting specific group: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_group_risk_score_history(self, group_id, full=False, **params):
        try:
            params = {**params, "full": "true"} if full else {}
            return self._get(f"/v1/groups/{group_id}/risk_score_history", params=params)
        except APIError as e:
            print(f"Error getting group risk score history: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_phishing_campaign(self, campaign_id, **params):
        try:
            return self._get(f"/v1/phishing/campaigns/{campaign_id}", params=params)
        except APIError as e:
            print(f"Error getting specific phishing campaign: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_all_phishing_security_tests(self, **params):
        try:
            return self._get("/v1/phishing/security_tests", params=params)
        except APIError as e:
            print(f"Error getting all phishing security tests: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_account_and_subscription_data(self, **params):
        try:
            return self._get("/v1/account", params=params)
        except APIError as e:
            print(f"Error getting account data: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_user(self, user_id, **params):
        try:
            return self._get(f"/v1/users/{user_id}", params=params)
        except APIError as e:
            print(f"Error getting specific user: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_users_in_group(self, group_id, **params):
        try:
            return self._get(f"/v1/groups/{group_id}/members", params=params)
        except APIError as e:
            print(f"Error getting users in group: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_all_users(self, **params):
        """
        Retrieves a list of all users in the KnowBe4 account.

        Parameters:
        params (dict): Optional query parameters (e.g., status, group_id).

        Returns:
        JSON response containing a list of users.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            return self._get("/v1/users", params=params)
        except APIError as e:
            print(f"Error getting all users: {e.message} {e.status_code} {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_account_risk_score_history(self, full=False, **params):
        """
        Retrieves the account's risk score history.

        Parameters:
        full (bool): Optional flag to include the entire risk score history.

        Returns:
        JSON response containing the account's risk score history.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            params = {"full": "true"} if full else {}
            return self._get("/v1/account/risk_score_history", params=params)
        except APIError as e:
            print(f"Error getting account risk score history: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_psts_from_specific_campaign(self, campaign_id, **params):
        """
        Retrieves all phishing security tests (PSTs) from a specific campaign.

        Parameters:
        campaign_id (int): The identifier of the phishing campaign.

        Returns:
        JSON response containing phishing security tests for the specified campaign.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            return self._get(
                f"/v1/phishing/campaigns/{campaign_id}/security_tests", params=params
            )
        except APIError as e:
            print(f"Error getting PSTs from specific campaign: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_phishing_security_test(self, pst_id, **params):
        """
        Retrieves data for a specific phishing security test.

        Parameters:
        pst_id (int): The identifier of the phishing security test.

        Returns:
        JSON response containing data of the specified phishing security test.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            return self._get(f"/v1/phishing/security_tests/{pst_id}", params=params)
        except APIError as e:
            print(f"Error getting specific phishing security test: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_all_recipient_results(self, pst_id, **params):
        """
        Retrieves a list of all recipients of a specific phishing security test.

        Parameters:
        pst_id (int): The identifier of the phishing security test.

        Returns:
        JSON response containing a list of recipients for the specified test.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            return self._get(
                f"/v1/phishing/security_tests/{pst_id}/recipients", params=params
            )
        except APIError as e:
            print(f"Error getting all recipient results: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_recipient_results(self, pst_id, recipient_id, **params):
        """
        Retrieves details about a specific user's phishing security test results.

        Parameters:
        pst_id (int): Identifier of the phishing security test.
        recipient_id (int): Identifier of the recipient (user).

        Returns:
        JSON response containing the specified recipient's phishing test results.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            endpoint = f"/v1/phishing/security_tests/{pst_id}/recipients/{recipient_id}"
            return self._get(endpoint, params=params)
        except APIError as e:
            print(f"Error getting specific recipient's results: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_all_store_purchases(self, **params):
        """
        Retrieves a list of all Store Purchases in the KnowBe4 account.

        Returns:
        JSON response containing a list of all store purchases.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            return self._get("/v1/training/store_purchases", params=params)
        except APIError as e:
            print(f"Error getting all store purchases: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_store_purchase(self, store_purchase_id, **params):
        """
        Retrieves a specific Store Purchase from the KnowBe4 account.

        Parameters:
        store_purchase_id (int): Identifier of the store purchase.

        Returns:
        JSON response containing data of the specified store purchase.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            endpoint = f"/v1/training/store_purchases/{store_purchase_id}"
            return self._get(endpoint, params=params)
        except APIError as e:
            print(f"Error getting specific store purchase: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_all_policies(self, **params):
        """
        Retrieves a list of all Policies in the KnowBe4 account.

        Returns:
        JSON response containing a list of all policies.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            return self._get("/v1/training/policies", params=params)
        except APIError as e:
            print(f"Error getting all policies: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_policy(self, policy_id, **params):
        """
        Retrieves a specific Policy from the KnowBe4 account.

        Parameters:
        policy_id (int): Identifier of the policy.

        Returns:
        JSON response containing data of the specified policy.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            endpoint = f"/v1/training/policies/{policy_id}"
            return self._get(endpoint, params=params)
        except APIError as e:
            print(f"Error getting specific policy: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_all_training_campaigns(self, **params):
        """
        Retrieves a list of all Training Campaigns in the KnowBe4 account.

        Returns:
        JSON response containing a list of all training campaigns.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            return self._get("/v1/training/campaigns", params=params)
        except APIError as e:
            print(f"Error getting all training campaigns: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_training_campaign(self, campaign_id, **params):
        """
        Retrieves a specific Training Campaign from the KnowBe4 account.

        Parameters:
        campaign_id (int): Identifier of the training campaign.

        Returns:
        JSON response containing data of the specified training campaign.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            endpoint = f"/v1/training/campaigns/{campaign_id}"
            return self._get(endpoint, params=params)
        except APIError as e:
            print(f"Error getting specific training campaign: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_all_training_enrollments(self, **params):
        """
        Retrieves a list of all Training Enrollments in the KnowBe4 account.

        Parameters:
        params (dict): Optional query parameters to filter enrollments.

        Returns:
        JSON response containing a list of all training enrollments.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            return self._get("/v1/training/enrollments", params=params)
        except APIError as e:
            print(f"Error getting all training enrollments: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_specific_training_enrollment(self, enrollment_id, **params):
        """
        Retrieves a specific Training Enrollment from the KnowBe4 account.

        Parameters:
        enrollment_id (int): Identifier of the training enrollment.

        Returns:
        JSON response containing data of the specified training enrollment.

        Raises:
        APIError: For API-specific errors.
        Exception: For other unexpected errors.
        """
        try:
            endpoint = f"/v1/training/enrollments/{enrollment_id}"
            return self._get(endpoint, params=params)
        except APIError as e:
            print(f"Error getting specific training enrollment: {e.message}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    # ... continue with other methods ...
