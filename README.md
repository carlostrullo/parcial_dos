
# Carlos Arturo Arredondo Trullo. Cod 12107001
##Solución parcial dos.

### A continuación se describiran los pasos utilizados para resolver el segundo parcial de sistemas operacionales
#### 1. ingrese como usuario root. Luego proceda a realizar la instalación de jenkins descrita en el tutorial https://www.youtube.com/watch?v=Jy6NfzlVAKg.

#### 2. Una vez instalado jenkins y realizada la prueba del test, con el ambiente activado cree un archivo llamado parcial.py (donde se usará el codigo del tutorial del parcial uno) y coloque el siguiente código

```py
from flask import Flask, abort, request
from subprocess import Popen, PIPE
import os
import json


app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/files',methods=['POST'])
def create_files():
  content = request.get_json(silent=True)
  filename = content['filename']
  content =  content['content']
  grep_process2 = open(filename+'.txt','a')
  grep_process2.write(content+'\n')
  grep_process2.close()
  return "el archivo ha sido creado",201

@app.route(api_url+'/files',methods=['GET'])
def get_list_files():
 path= '/home/filesystem_user/'
 list = []
 lstDir =os.walk(path)
 for root,dirs,files in lstDir:
     for fichero in files:
        (nombreFichero,extension)=os.path.splitext(fichero)
        if(extension==".txt"):
           list.append(nombreFichero+extension)
 return json.dumps(list)



@app.route(api_url+'/files',methods=['DELETE'])
def delete_files():
 process1 = os.system('cd /home/filesystem_user')
 process2 = os.system('find . -name "*.txt" -type f -delete')
 return "los archivos txt han sido eliminados",200


@app.route(api_url+'/files',methods=['PUT'])
def request_put():
  return "HTTP 404 not found",404

@app.route(api_url+'/files/recently_created',methods=['GET'])
def request_get():
 process1 = Popen(["grep","/bin/bash","/home/filesystem_user","find / -type f -mtime -0"], stdout=PIPE, stderr=PIPE)
 process3 = Popen(["awk",'-F',':','{print $1}'], stdin=process1.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
 list = {}
 list["files"] = filter(None,process3)
 return json.dumps(list), 200



@app.route(api_url+'/files/recently_created',methods=['POST'])
def request_post():
  return "HTTP 404 not found",404

@app.route(api_url+'/files/recently_created',methods=['PUT'])
def request_put_one():
  return "HTTP 404 not found",404

@app.route(api_url+'/files/recently_created',methods=['DELETE'])
def request_delete_one():
  return "HTTP 404 not found",404


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')

```
#### 3. luego cree un archivo llamado test.py, donde se almacenará el codigo de prueba implementado con pytest (es el que está a continuación)

```py
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
```

#### 4. A continuación se abre una ventana o pestaña nueva en el navegador web, se ingresa la dirección ip mas el puerto, tal cual como se muestra a continuación.

// imagen ingreso a jenkins

#### 5. se da click en nueva tarea, se seleciona "crear un proyecto de estilo libre" y se coloca un nombre (puede ser de su preferencia).
//imagen crear proyecto

#### 6. A partir de este punto empiezan las configuraciones de la prueba con jenkins. el primer paso es especificar que tipo de proyecto es y donde se encuentra

// github project

#### 7. Luego seleccionar el origen del código
//codigo fuente


#### 8. Se fija cada cuanto tiempo se va ejecutar la prueba

// tiempo

#### 9. código shell
//

#### 10. código shell
#### 11. cobertura

#### 12. htmlcov
#### 13. xml Junit
#### 14. contruir ahora
#### 15. contruir ahora











