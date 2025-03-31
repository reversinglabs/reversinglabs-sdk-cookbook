# ReversingLabs SDK Spectra Detect module (tiscale) examples

This directory contains code examples demonstrating the use of the ReversingLabs SDK's Spectra Detect module (tiscale). 
The tiscale module uses the Spectra Detect appliance's REST API to perform sample analysis tasks and fetch analysis results.
All code examples are arranged into Jupyter notebooks.

### What is the tiscale module?
The tiscale module of the ReversingLabs SDK enables the user to automate the use of Spectra Detect's REST API through Python code.  
Python classes and functions defined in that module enable easy API object creation, input parameter validation, request sending and error handling.
The ReversingLabs SDK in its entirety can be used for creating standalone scripts and services or as part of other platforms and engines that need to connect to the ReversingLabs platform.

### Authentication
Spectra Detect uses **token** authentication.
When using the ReversingLabs SDK tiscale module you only need to provide your authentication token as a string while creating the Spectra Detect API object and the SDK will format the required "Authorization" headers for you.

To obtain the required credentials, visit https://www.reversinglabs.com/products/spectra-detect  

#### Storing and using the credentials
We will store our Spectra Detect credentials in a **local file** and then load them in our code.

1. Create a JSON file named `tiscale_credentials.json` in this current folder.
2. Create the following data in that file and replace the placeholder value with your actual host and token:
    ```json
    {
      "host": "your_tiscale_host",
      "token": "your_tiscale_api_token"
    }
    ```
3. Save the file.

**NOTE:** The `tiscale_credentials.json` file must have this exact structure to work.

Instead of doing this step and loading the credentials from the file, 
you can paste your credentials directly into the Python code everytime you create an API object.
To see learn how to do that, see the below example of an API object.


### Creating an API object 
Currently, the tiscale module has only one Python class: TitaniumScale 
To create an object, perform the following step:  

```python
from ReversingLabs.SDK.tiscale import TitaniumScale


tiscale_obj = TitaniumScale(
    host="url_of_tiscale_instance",
    token="your_actual_token",
    user_agent="My company name here",
    verify=True
)
```

**Explanation:**
- `host` - Host URL of your Spectra Detect instance, including the http/https protocol prefix
- `token` - Token for the Spectra Detect instance API
- `user_agent` - A string that describes the sender of requests (optional)
- `verify` - Should the server certificates bi verified or not

Now that you have an API object, you can proceed to call any of the available methods that the object contains.  
To see specific usage examples or recommended scenarios for certain API-s, check the provided **notebooks**
(**ipynb** files).


## Advanced
### Error handling
To understand this section better, **learn about creating API requests first** by reading the notebooks in the Spectra Detect folder.  
Each module raises corresponding custom exceptions according to the error status code returned in the response. 
Custom exception classes that correspond to error status codes also carry the original response object in its entirety. 
To learn how to fetch and use the response object out of the exception object, see the following example.

```python
from ReversingLabs.SDK.tiscale import TitaniumScale


tiscale_obj = TitaniumScale(
    host="url_of_tiscale_instance",
    token="your_actual_token",
    user_agent="My company name here",
    verify=True
)

try:
    resp = tiscale_obj.get_processing_task_info(
       task_id=12345,
       full=True,
    )
except Exception as e:
    if hasattr(e, "response_object"):
        print(e.response_object.content)
    else:
        raise 
```