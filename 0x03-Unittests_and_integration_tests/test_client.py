#!/usr/bin/env python3
"""
Test cases for GithubOrgClient class
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
import json


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"login": "test_org"})
    def test_org(self, org_name, mock_get_json):
        """
            Test GithubOrgClient.org method
        """
        client = GithubOrgClient(org_name)
        org_info = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(org_info, {"login": "test_org"})

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos method
        """
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = \
                        "https://api.github.com/orgs/test_org/repos"

            client = GithubOrgClient("test_org")
            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos"
                )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": {}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
            Test GithubOrgClient.has_license method
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
