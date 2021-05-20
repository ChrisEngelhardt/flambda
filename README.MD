# Flambda
Place your code into the lambda functions folder. Run the container.
All functions will be callable as REST API. Function input and output will be of type json.
For convenience, if you open the hosted [Flambda container](https://127.0.0.1:5000) from your browser you can see your created endpoints.


# Lambda Functions
Lambda functions must be placed in the lambda folder and must have a `main(j)` method that returns json serializable object. The paramter j is the json deserialized object given from the http body. Each function must be placed into its own folder and the python code file must me named like the folder. 

Structure:
```
├── lambdas
│   └── exmapleFunction
│       └── exmapleFunction.py
```

Example Code:
```
import time
def main():
  time.sleep(3)
  return { 
    'success': True
  }
```

If you don't need further dependencies, you can simply run `docker run -p 5000:5000 -v ${PWD}/lambdas:/app/lambdas chrisengelhardt/flambda`. 

Otherwise you need to create a own container that inherits from `chrisengelhardt/flambda`.
For this create a requirements.txt and place all needed dependencies in it.

Example Dockerfile to build a container with own dependencies

```
FROM chrisengelhardt/flambda

# COPY requirements.txt /app/requirements.txt #*Option 1
COPY lambdas /app/lambdas
RUN pip3 install --no-cache-dir -r /app/requirements.txt
WORKDIR /app/
CMD [ "python", "main.py" ]
```
 and build with `docker build -t YOURIMAGENAME .`

## Remarks:
- *Option 1: If you build your own container you can also bundle your lambda functions into the container and thus can simply run `docker run -p 5000:5000  YOURIMAGENAME`. This makes the docker code much more straight forward to start. However if you chance the lambda functions the code will not be able to hot reload as with the mounted volume `docker run -p 5000:5000 -v ${PWD}/lambdas:/app/lambdas YOURIMAGENAME`. 

