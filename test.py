import pytest
import requests
import json

host = "https://cmpapi.imina.cat"
userid = '1'
path = 'user'

# Pretty basic tests, the tests can be a little bit more advanced, but for this test i should be enough.

def test_add_user():
    global userid
    # If we'll add additional headers.
    headers = {}
    # If we'll add additional payload.
    payload = {}

    url = host + '/'+ path
    resp = requests.request("POST", url, headers=headers, data=payload)
    # Validate response status code if it is 201 content created successfully
    response = resp.text
    userid = response.split()[5]
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

