import pytest
import requests
import json

host = "http://localhost:80"
userid = '1'
path = 'user'

# Pretty basic tests, the user id should be dynamic, and the test can be a little bit more advanced, but for this test i should be enough.

def test_add_user():
    # If we'll add additional headers.
    headers = {}
    # If we'll add additional payload.
    payload = {}
    
    url = host + '/'+ path
    resp = requests.request("POST", url, headers=headers, data=payload)
    # Validate response status code if it is 201 content created successfully
    assert resp.status_code == 201

def test_recive_user():
    # If we'll add additional headers.
    headers = {}
    # If we'll add additional payload.
    payload = {}
    
    url = host + '/' + path + '/' + userid
    resp = requests.request("GET", url, headers=headers, data=payload)
    # Validate response status code if it is 200, and the content is diferent to None everything is ok.
    assert resp.status_code == 200
    content = resp.text.split()
    assert content[2] != 'None'

def test_delete_user():
    # If we'll add additional headers.
    headers = {}
    # If we'll add additional payload.
    payload = {}
    
    url = host + '/' + path + '/' + userid
    resp = requests.request("DELETE", url, headers=headers, data=payload)
    # Validate response status code if it is 200, deleted complete, if is it 404 throw an error.
    assert resp.status_code == 200

def test_all_users():
    # If we'll add additional headers.
    headers = {}
    # If we'll add additional payload.
    payload = {}
    
    url = host + '/allusers'
    resp = requests.request("GET", url, headers=headers, data=payload)
    # Validate response status code if it is 200, and the content is diferent to None everything is ok.
    assert resp.status_code == 200