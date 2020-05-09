import requests
import unittest


class RequestsTest(unittest.TestCase):
    """Container for all requests tests."""

    url = "https://jsonplaceholder.typicode.com/photos"
    new_url = "https://jsonplaceholder.typicode.com/photos/100"
    jsonPayload = {'album': 1, 'title': 'test'}

    def test_get_request(self):
        response = requests.get(self.url)
        print(response.status_code)

    def test_post_request(self):
        response = requests.post(self.url, json=self.jsonPayload)
        response.json()

    def test_put_request(self):
        response = requests.put(self.new_url, json=self.jsonPayload)
        response.json()

    def test_delete_request(self):
        response = requests.delete(self.new_url)
        response.json()


if __name__ == '__main__':
    unittest.main()





