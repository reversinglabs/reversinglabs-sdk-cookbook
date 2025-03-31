# ReversingLabs SDK Spectra Analyze module (a1000) examples

This directory contains code examples demonstrating the use of the ReversingLabs SDK's Spectra Analyze module (a1000). 
The a1000 module uses the Spectra Analyze appliance's REST API to perform sample analysis tasks, fetch analysis results and many other actions.
All code examples are arranged into Jupyter notebooks.

### What is the a1000 module?
The a1000 module of the ReversingLabs SDK enables the user to automate the use of Spectra Analyze's REST API through Python code.  
Python classes and functions defined in that module enable easy API object creation, input parameter validation, request sending and error handling.
The ReversingLabs SDK in its entirety can be used for creating standalone scripts and services or as part of other platforms and engines that need to connect to the ReversingLabs platform.

### Authentication
Spectra Analyze uses **token** authentication.
When using the ReversingLabs SDK a1000 module you only need to provide your authentication token as a string while creating the Spectra Analyze API object and the SDK will format the required "Authorization" headers for you.
While creating the API object, you can either pass in the **token** or your Spectra Analyze **username and password** to authorize your requests.

**NOTE:** Using the token is the preferred way since using the username and password pair performs an additional request in the background to obtain the token. That being said, **the token is the recommended way of authorizing your requests on the Spectra Analyze**.

To obtain the required credentials, visit https://www.reversinglabs.com/products/malware-threat-hunting-and-investigations  

#### Storing and using the credentials
We will store our Spectra Analyze credentials in a **local file** and then load them in our code.

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
- `host` - Host URL of your Spectra Analyze instance, including the http/https protocol prefix
- `token` - Your authorization token for the Spectra Analyze instance
- `user_agent` - A string that describes the sender of requests (optional)
- `verify` - Should the server certificates bi verified or not

Now that you have an API object, you can proceed to call any of the available methods that the object contains.  
To see specific usage examples or recommended scenarios for certain API-s, check the provided **notebooks**
(**ipynb** files).


## Advanced
### Error handling
To understand this section better, **learn about creating API requests first** by reading the notebooks in the Spectra Analyze folder.  
Each module raises corresponding custom exceptions according to the error status code returned in the response. 
Custom exception classes that correspond to error status codes also carry the original response object in its entirety. 
To learn how to fetch and use the response object out of the exception object, see the following example.

```python
from ReversingLabs.SDK.a1000 import A1000


a1000_obj = A1000(
    host="url_of_a1000_instance",
    token="your_actual_token",
    verify=True
)

try:
    resp = a1000_obj.get_classification_v3(
        sample_hash="cf23df2207d99a74fbe169e3eba035e633b65d94",
        av_scanners=True
    )
except Exception as e:
    if hasattr(e, "response_object"):
        print(e.response_object.content)
    else:
        raise 
```