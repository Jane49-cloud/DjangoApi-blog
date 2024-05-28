import requests
import pytest
from unittest import mock

BASE_URL = "http://localhost:8000/api"  

def test_create_blog():
    url = f"{BASE_URL}/blogs/create"
    headers = {
        "Authorization": "JWT  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NDU1ODg0LCJpYXQiOjE3MTY4NjM4ODQsImp0aSI6IjNiOGE5ODdkODU3ODRmYjlhZDZkMGY4OWZiNWRkMmRkIiwidXNlcl9pZCI6OTcwNDU4OTgyNjYwNDA3Mjk3fQ.dgp6L7Tyy4RYuNlRYJPufHsZgjE7JpHtZJWnF7nONnY"  
    }
    data = {
        "title": "Test Blog",
        "content": "This is a test blog content.",
        "description":"sample description",
        "category":"970657784744214529",
        
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Blog"

def test_list_blogs():
    url = f"{BASE_URL}/blogs/all"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_blog_details():
    blog_id = 970658229127774209
    url = "http://127.0.0.1:8000/api/blogs/970658229127774209"
    response = requests.get(url)
    
    # Debugging step: print the URL and response content
    print(f"Request URL: {url}")
    print(f"Response content: {response.content}")
    
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
    response_json = response.json()
    print(f"Response JSON: {response_json}")
    
    assert response_json["id"] == str(blog_id), f"Expected blog ID {blog_id} but got {response_json['id']}"


def test_update_blog():
    blog_id = 971333204973780993
    url = "http://127.0.0.1:8000/api/blogs/971333204973780993"
    headers = {
        "Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NDU1ODg0LCJpYXQiOjE3MTY4NjM4ODQsImp0aSI6IjNiOGE5ODdkODU3ODRmYjlhZDZkMGY4OWZiNWRkMmRkIiwidXNlcl9pZCI6OTcwNDU4OTgyNjYwNDA3Mjk3fQ.dgp6L7Tyy4RYuNlRYJPufHsZgjE7JpHtZJWnF7nONnY"  # Replace with a valid token
    }
    data = {
        "title": "Updated Blog Title"
    }
    response = requests.patch(url, headers=headers, json=data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Blog Title"

def test_delete_blog():
    blog_id = "972559111295860737"
    url = "http://127.0.0.1:8000/api/blogs/972557278173921281"
    headers = {
        "Authorization": "JWT  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NDU1ODg0LCJpYXQiOjE3MTY4NjM4ODQsImp0aSI6IjNiOGE5ODdkODU3ODRmYjlhZDZkMGY4OWZiNWRkMmRkIiwidXNlcl9pZCI6OTcwNDU4OTgyNjYwNDA3Mjk3fQ.dgp6L7Tyy4RYuNlRYJPufHsZgjE7JpHtZJWnF7nONnY"  # Replace with a valid token
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204

if __name__ == "__main__":
    pytest.main()
