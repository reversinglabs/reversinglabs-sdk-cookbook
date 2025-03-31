# ReversingLabs SDK Spectra Intelligence module (ticloud) examples

This directory contains code examples for using several popular Spectra Intelligence API-s arranged into Jupyter notebooks.

### What is the ticloud module?
The ticloud module enables the user to harvest the benefits of Spectra Intelligence API-s through Python code.  
Python classes and functions defined in that module enable easy API object creation, input parameter validation, request sending and error handling.
The ReversingLabs SDK in its entirety can be used for creating standalone scripts and services or as part of other platforms and engines that need to connect to the ReversingLabs platform.

### Authentication
Spectra Intelligence uses a **username and password** pair (**basic authentication**).  
You can pass in your credentials while creating the desired API object.  
To obtain the required credentials, visit https://www.reversinglabs.com/products/file-reputation-service  
Each username can have a certain number of roles for API-s assigned to it. In case your username does not have the required role for your desired action, you will receive an error stating so.  

#### Storing and using the credentials
We will store our Spectra Intelligence credentials in a **local file** and then load them in our code.

1. Create a JSON file named `ticloud_credentials.json` in this current folder.
2. Create the following data in that file and replace the placeholder values with your actual username and password:
    ```json
    {
      "username": "your_actual_username",
      "password": "your_actual_password"
    }
    ```
3. Save the file.

**NOTE:** The `ticloud_credentials.json` file must have this exact structure to work.

Instead of doing this step and loading the credentials from the file, 
you can paste your credentials directly into the Python code everytime you create an API object.
To see learn how to do that, see the below example of an API object.


### Creating an API object
Each Spectra Intelligence API has its own class.  
To create an object, same parameters are required in all cases.  

**Example:**

```python
from ReversingLabs.SDK.ticloud import FileReputation


file_reputation = FileReputation(
    host="https://data.reversinglabs.com",
    username="u/example_user",
    password="ExaMplePassWorD",
    user_agent="My company name here"
)
```

**Explanation:**
- `host` - Host URL of the Spectra Intelligence. The most widely used one is `data.reversinglabs.com`
- `username` - Your Spectra Intelligence account username with the required roles for the API that you want to use
- `password` - The password for your Spectra Intelligence username
- `user_agent` - A string that describes the sender of requests (optional)

Now that you have an API object, you can proceed to call any of the available methods that the object contains.  
To see specific usage examples or recommended scenarios for certain API-s, check the provided **notebooks**
(**ipynb** files).


## Advanced
### Error handling
To understand this section better, **learn about creating API requests first** by reading the notebooks in the Spectra Intelligence folder.  
Each module raises corresponding custom exceptions according to the error status code returned in the response. 
Custom exception classes that correspond to error status codes also carry the original response object in its entirety. 
To learn how to fetch and use the response object out of the exception object, see the following example.

```python
from ReversingLabs.SDK.ticloud import FileReputation


file_rep = FileReputation(
    host="https://data.reversinglabs.com",
    username="u/username",
    password="password"
)

try:
    resp = file_rep.get_file_reputation(hash_input="cf23df2207d99a74fbe169e3eba035e633b65d94")
except Exception as e:
    if hasattr(e, "response_object"):
        print(e.response_object.content)
    else:
        raise  
```