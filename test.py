from flask import Flask, abort, request
import os
import json
import pytest
import parcial
import httplib, urllib


@pytest.fixture
def app():
    return parcial.app

@pytest.fixture
def test_client(app):
    return app.test_client()


def test_files_post():
  content= {"filename": "escribe2","content": "prueba archivo"}
  data_json=json.dumps(content)
  headers = {'content-type': 'application/json'}
  conn = httplib.HTTPConnection("localhost:8088")
  conn.request('POST','/v1.0/files',data_json, headers)
  response=conn.getresponse()
  assert response.status==201
  conn.close()


def test_files_get():
  conn = httplib.HTTPConnection("localhost:8088")
  conn.request('GET','/v1.0/files')
  response=conn.getresponse()
  assert response.status==200
  conn.close()


def test_files_delete():
  conn = httplib.HTTPConnection("localhost:8088")
  conn.request('DELETE','/v1.0/files')
  response=conn.getresponse()
  assert response.status==200
  conn.close()
    

def test_files_put():
  conn = httplib.HTTPConnection("localhost:8088")
  conn.request('PUT','/v1.0/files')
  response=conn.getresponse()
  assert response.status==404
  conn.close()

def test_files_recently_created():
  conn = httplib.HTTPConnection("localhost:8088")
  conn.request('GET','/v1.0/files/recently_created')
  response=conn.getresponse()
  assert response.status==200
  conn.close()

def test_files_recently_created_post():
  conn = httplib.HTTPConnection("localhost:8088")
  conn.request('POST','/v1.0/files/recently_created')
  response=conn.getresponse()
  assert response.status==404
  conn.close()


def test__files_recently_created_put():
  conn = httplib.HTTPConnection("localhost:8088")
  conn.request('PUT','/v1.0/files/recently_created')
  response=conn.getresponse()
  assert response.status==404
  conn.close()



def test__files_recently_created_delete():
  conn = httplib.HTTPConnection("localhost:8088")
  conn.request('DELETE','/v1.0/files/recently_created')
  response=conn.getresponse()
  assert response.status==404
  conn.close()
