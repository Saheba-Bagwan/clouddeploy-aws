import unittest

from app.app import app


class CloudDeployTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_homepage_returns_success(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"CloudDeploy AWS", response.data)

    def test_health_endpoint_returns_success(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)

    def test_health_endpoint_returns_expected_data(self):
        response = self.client.get("/health")

        data = response.get_json()

        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["application"], "CloudDeploy AWS")


if __name__ == "__main__":
    unittest.main()