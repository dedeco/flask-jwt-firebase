# Flask JWT Firebase

## Run api local

1.  How do I get set up this api? Install python +3.7 and create a virtualenv using pipenv:
    [See here how to](https://github.com/pypa/pipenv).

2.  Create and running a virtualenv
    ```
    user@server:~$ virtualenv flask-jwt-env3
    user@server:~$ source flask-jwt-env3/bin/activate
    ```
3. Running api App:
    ```
    (flask-jwt-env3) user@server:~$ FLAKS_APP=app.py
    (flask-jwt-env3) user@server:~$ flask run
    ```
    
    The api will be available on http://0.0.0.0:8080/
    
    A GET request example
    
    ``` 
    curl http://0.0.0.0:8080/ -H "Authorization: Bearer <VALID_TOKEN>" 
    ```

    RESPONSE:
    ``` 
    {
        "hello": "world"
    }
    ``` 
