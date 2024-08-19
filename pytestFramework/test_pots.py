import requests
import json
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_post_validRequest (self, dataBaseUrl, jsonData, jsonDataResponse):
        validBaseURL, _ = dataBaseUrl
        url = validBaseURL
        print("post url:" + url)
        data = jsonData
        response = requests.post(url, json=data)
        assert response.status_code == 201, f"Expected status code 404, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)
        user_id = json_data["id"]
        expectedPostuserId, expectedPostTitle, expectedBody = jsonDataResponse
        assert json_data["userId"] == int(expectedPostuserId), f"Expected userId {expectedPostuserId}, but got {json_data.get('userId')}"
        assert json_data["title"] == expectedPostTitle, f"Expected userId {expectedPostTitle}, but got {json_data.get('title')}"
        assert json_data["body"] == expectedBody, f"Expected userId {expectedBody}, but got {json_data.get('body')}"
        return user_id

    def test_post_invalidUrl (self, dataBaseUrl,jsonData):
        _, invalidBaseURL = dataBaseUrl
        url = invalidBaseURL
        print("post url:" + url)
        data = jsonData
        response = requests.post(url, json=data)
        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
        print(f"Response Status Code: {response.status_code}")
        json_data = response.json()
        json_str = json.dumps(json_data, indent=1)
        print("json response body:", json_str)