# ReversingLabs SDK A1000 module (a1000) examples

This directory contains code examples demonstrating the use of the ReversingLabs SDK's A1000 module (a1000). 
The a1000 module uses the A1000 appliance's REST API to perform sample analysis tasks, fetch analysis results and many other actions.
All code examples are arranged into Jupyter notebooks.

### What is the a1000 module?
The a1000 module of the ReversingLabs SDK enables the user to automate the use of A1000's REST API through Python code.  
Python classes and functions defined in that module enable easy API object creation, input parameter validation, request sending and error handling.
The ReversingLabs SDK in its entirety can be used for creating standalone scripts and services or as part of other platforms and engines that need to connect to the ReversingLabs platform.

### Authentication
A1000 uses **token** authentication.
When using the ReversingLabs SDK a1000 module you only need to provide your authentication token as a string while creating the A1000 API object and the SDK will format the required "Authorization" headers for you.
While creating the API object, you can either pass in the **token** or your A1000 **username and password** to authorize your requests.

**NOTE:** Using the token is the preferred way since using the username and password pair performs an additional request in the background to obtain the token. That being said, **the token is the recommended way of authorizing your requests on the A1000**.

To obtain the required credentials, visit https://www.reversinglabs.com/products/malware-threat-hunting-and-investigations  

#### Storing and using the credentials
We will store our A1000 credentials in a **local file** and then load them in our code.

1. Create a JSON file named `a1000_credentials.json` in this current folder.
2. Create the following data in that file and replace the placeholder value with your actual token:
    ```json
    {
      "token": "your_actual_token",
      "username": "your_actual_username",
      "password": "your_actual_password"
    }
    ```
3. Save the file.

**NOTE:** The `a1000_credentials.json` file must have this exact structure to work.

Instead of doing this step and loading the credentials from the file, 
you can paste your credentials directly into the Python code everytime you create an API object.
To see learn how to do that, see the below example of an API object.


### Creating an API object 
Currently, the a1000 module has only one Python class: A1000 
To create an object, perform the following step:  

```python
from ReversingLabs.SDK.a1000 import A1000


a1000_obj = A1000(
    host="url_of_a1000_instance",
    token="your_actual_token",
    user_agent="My company name here",
    verify=True
)
```

**Explanation:**
- `host` - Host URL of your A1000 instance, including the http/https protocol prefix
- `token` - Your authorization token for the A1000 instance
- `user_agent` - A string that describes the sender of requests (optional)
- `verify` - Should the server certificates bi verified or not

Now that you have an API object, you can proceed to call any of the available methods that the object contains.  
To see specific usage examples or recommended scenarios for certain API-s, check the provided **notebooks**
(**ipynb** files).