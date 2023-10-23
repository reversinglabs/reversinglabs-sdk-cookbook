# ReversingLabs SDK Cloud Deep Scan module (clouddeepscan) examples

This directory contains code examples demonstrating the use of the ReversingLabs SDK's Cloud Deep Scan module (clouddeepscan).  
The Cloud Deep Scan File Analysis service is a cloud-based security solution that detects malicious  content and threats using the ReversingLabs static analysis engine integrated with  an extensive file reputation source database.
The clouddeepscan module uses Cloud Deep Scan's REST API to perform sample analysis tasks, fetch analysis results and many other actions.
All code examples are arranged into Jupyter notebooks.

### What is the clouddeepscan module?
The clouddeepscan module of the ReversingLabs SDK enables the user to automate the use of Cloud Deep Scan's REST API through Python code.  
Python classes and functions defined in that module enable easy API object creation, input parameter validation, request sending and error handling.
The ReversingLabs SDK in its entirety can be used for creating standalone scripts and services or as part of other platforms and engines that need to connect to the ReversingLabs platform.

### Authentication
To use Cloud Deep Scan through the ReversingLabs SDK, you need to obtain several credentials from your instance od Cloud Deep Scan. To do so, go to "Settings" and then "REST API Authorization" on your Cloud Deep Scan web GUI.
There you will find instructions on how to obtain the required credentials:
- Client ID
- Client Secret
- Token Endpoint
- REST API Hostname  

**NOTE:** To obtain a client ID and a client secret, you need to create an Application Client first.

#### Storing and using the credentials
We will store our obtained Cloud Deep Scan credentials in a **local file** and then load them in our code.

1. Create a JSON file named `deepscan_credentials.json` in this current folder.
2. Create the following data in that file and replace the placeholder value with your actual token:
    ```json
    {
      "rest_hostname": "rest_api_hostname",
      "token_endpoint": "token_endpoint",
      "client_id": "your_client_id",
      "client_secret": "your_client_secret"
    }
    ```
3. Save the file.

**NOTE:** The `deepscan_credentials.json` file must have this exact structure to work.

Instead of doing this step and loading the credentials from the file, 
you can paste your credentials directly into the Python code everytime you create an API object.
To see learn how to do that, see the below example of an API object.


### Creating an API object 
To create a CloudDeepScan object, perform the following step:  

```python
from ReversingLabs.SDK.clouddeepscan import CloudDeepScan


deepscan_obj = CloudDeepScan(
   rest_hostname="rest_api_hostname",
   token_endpoint="token_endpoint",
   client_id="your_client_id",
   client_secret="your_client_secret"
)
```

**Explanation:**
- `rest_hostname` - The REST API hostname which represents the base URL of all Cloud Deep Scan API endpoints.
- `token_endpoint` - The endpoint used to fetch the authorization token
- `client_id` - The ID of your OAuth2.0 client used for authorization
- `client_secret` - The secret of your OAuth2.0 client used for authorization

Now that you have an API object, you can proceed to call any of the available methods that the object contains.  
To see specific usage examples or recommended scenarios for certain API-s, check the provided **notebooks**
(**ipynb** files).