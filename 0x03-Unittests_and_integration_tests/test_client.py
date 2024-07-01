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

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(org_info, {"login": "test_org"})

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
            Test Method
        """
        """Test GithubOrgClient._public_repos_url property"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        client = GithubOrgClient("test_org")
        result = client._public_repos_url

        mock_org.assert_called_once()
        self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")

    
if __name__ == "__main__":
    unittest.main()
