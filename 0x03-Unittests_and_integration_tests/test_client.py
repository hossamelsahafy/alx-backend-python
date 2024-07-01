#!/usr/bin/env python3
"""
Test cases for GithubOrgClient class
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"login": "test_org"})
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""
        client = GithubOrgClient(org_name)
        org_info = client.org

        # Assert that get_json was called exactly once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert that the returned org_info matches the expected mocked value
        self.assertEqual(org_info, {"login": "test_org"})


if __name__ == "__main__":
    unittest.main()
