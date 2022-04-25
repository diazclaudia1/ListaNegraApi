import unittest
import json
from apiritif import http
import requests
import logging

   

# some JSON:
login_body_ok =  {"username":"admin1","password":"admin1"}
login_body_error =  {"username":"5555","password":"5555"}
signup_body_ok = {"username":"admin111","password1":"admin111","password2":"admin111"}
signup_body_error = {"username":"admin1","password1":"admin1","password2":"123456"}
blacklist_body = {"email":"admin1","blocked_reason":"admin1"}

endpoint = "http://listanegra-env-3.eba-fecwesmv.us-east-1.elasticbeanstalk.com/"

def test_get_hello_world_ok():
    response = http.get(endpoint)
    response.assert_ok()
    response.assert_status_code(200)

def test_post_login_ok():
    response = http.post(endpoint+"auth/login",json=login_body_ok)
    response.assert_ok()
    response.assert_in_body("Successful login")
    response.assert_status_code(200)

def test_post_login_error():
    response = http.post(endpoint+"auth/login",json=None)
    response.assert_failed()
    response.assert_status_code(500)

def test_post_login_error():
    response = http.post(endpoint+"auth/login",json=login_body_error)
    response.assert_failed()
    response.assert_status_code(404)

def test_post_singup_ok():
    response = http.post(endpoint+"auth/signup",json=signup_body_ok)
    response.assert_ok()
    response.assert_status_code(200)
    response.assert_in_body("User created successfully")

def test_post_singup_error():
    response = http.post(endpoint+"auth/signup",json=signup_body_error)
    response.assert_failed()
    response.assert_status_code(400)
    response.assert_in_body("Password do not match")

def test_get_listanegra_ok():
    login = requests.post(endpoint+"auth/login", json = login_body_ok)
    jsonResponse = login.json() 
    print(jsonResponse["token"])   
    response = http.get(endpoint+"blacklists/admin", headers={'Authorization': "Bearer "+jsonResponse["token"]})
    response.assert_ok()
    response.assert_status_code(200)

def test_get_listanegra_token_error(): 
    response = http.get(endpoint+"blacklists/admin", headers={'Authorization': "Bearer "})
    response.assert_failed()
    response.assert_status_code(422)

def test_get_listanegra_not_exists():
    login = requests.post(endpoint+"auth/login", json = login_body_ok)
    jsonResponse = login.json() 
    print(jsonResponse["token"])   
    response = http.get(endpoint+"blacklists/admin123", headers={'Authorization': "Bearer "+jsonResponse["token"]})
    response.assert_failed()
    response.assert_status_code(404)

def test_post_addlistanegra_ok():
    login = requests.post(endpoint+"auth/login", json = login_body_ok)
    jsonResponse = login.json() 
    print(jsonResponse["token"])   
    response = http.post(endpoint+"blacklists", headers={'Authorization': "Bearer "+jsonResponse["token"]}, json=blacklist_body)
    response.assert_ok()
    response.assert_status_code(200)

def test_post_addlistanegra_error():
    login = requests.post(endpoint+"auth/login", json = login_body_ok)
    jsonResponse = login.json() 
    print(jsonResponse["token"])   
    response = http.post(endpoint+"blacklists", headers={'Authorization': "Bearer "+jsonResponse["token"]}, json=None)
    response.assert_failed()
    response.assert_status_code(500)

def test_get_listanegra_token_error(): 
    response = http.get(endpoint+"blacklists", headers={'Authorization': "Bearer "})
    response.assert_failed()
    response.assert_status_code(405)



