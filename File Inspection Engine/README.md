# ReversingLabs SDK File Inspection Engine module (fie) examples

This directory contains code examples demonstrating the use of the ReversingLabs SDK's File Inspection Engine module (fie). 
The fie module uses the File Inspection Engine's REST API to perform fast sample analysis tasks and fetch analysis results from the engine.
All code examples are arranged into Jupyter notebooks.

### What is the fie module?
The fie module of the ReversingLabs SDK enables the user to automate the use of File Inspection Engine's REST API through Python code.  
Python classes and functions defined in that module enable easy API object creation, request sending and error handling.
The ReversingLabs SDK in its entirety can be used for creating standalone scripts and services or as part of other platforms and engines that need to connect to the ReversingLabs platform.

### Authentication and license
File Inspection Engine (FIE) uses no authentication by default.  
The users need to take care of placing the FIE instance into secure part of their network.  
The FIE does, however, require a valid license to function.

To obtain the license, visit reversinglabs.com

#### Storing and using the host
We will store our File Inspection Engine host address in a **local file** and then load it in our code. This will give us flexibility for any future credential changes.

1. Create a JSON file named `fie_credentials.json` in this current folder.
2. Create the following data in that file and replace the placeholder value with your actual host:
    ```json
    {
      "host": "http://your_fie_host"
    }
    ```
3. Save the file.

**NOTE:** The `fie_credentials.json` file must have this exact structure to work.

Instead of doing this step and loading the credentials from the file, 
you can paste your credentials directly into the Python code everytime you create an API object.
To see learn how to do that, see the below example of an API object.


### Creating an API object 
Currently, the fie module has only one Python class: `FileInspectionEngine` 
To create an object, perform the following step:  

```python
from ReversingLabs.SDK.fie import FileInspectionEngine


fie_obj = FileInspectionEngine(
    host="url_of_fie_instance",
    user_agent="My company name here",
    verify=True
)
```

**Explanation:**
- `host` - Host URL of your FIE instance, including the http/https protocol prefix
- `user_agent` - A string that describes the sender of requests (optional)
- `verify` - Should the server certificates bi verified or not

Now that you have an API object, you can proceed to call any of the available methods that the object contains.  
To see specific usage examples or recommended scenarios for certain API-s, check the provided **notebooks**
(**ipynb** files).


## Advanced
### Error handling
To understand this section better, **learn about creating API requests first** by reading the notebooks in the File Inspection Engine folder.  
Each module raises corresponding custom exceptions according to the error status code returned in the response. 
Custom exception classes that correspond to error status codes also carry the original response object in its entirety. 
To learn how to fetch and use the response object out of the exception object, see the following example.

```python
from ReversingLabs.SDK.fie import FileInspectionEngine


fie_obj = FileInspectionEngine(
    host="url_of_fie_instance",
    user_agent="My company name here",
    verify=True
)

try:
    resp = fie_obj.scan_using_file_path(
       file_path="/path/to/local/file"
    )
except Exception as e:
    if hasattr(e, "response_object"):
        print(e.response_object.content)
    else:
        raise 
```