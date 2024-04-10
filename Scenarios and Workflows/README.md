# Scenarios and Workflows

This directory contains useful examples of analysis workflows and examples.  
In order to see how to put ReversingLabs SDK functionalities to good use in real-life scenarios, follow this readme and choose a desired notebook.


### Using the notebooks
Each notebook in this directory contains instructions and code snippets gathered around a certain type of usecase, analysis scenario or workflow.  
To use a selected notebook, open it and run each code snippet one by one. See the following authentication instructions to learn how to store and use your ReversingLabs credentials. 


### Authentication
Since this directory, at some point, uses all ReversingLabs SDK modules, the `credentials.json` file needs to contain credentials for all of them.
- TitaniumCloud uses a **username and password** pair (**basic authentication**).  
- A1000 uses a **token**. 
- TitaniumScale uses a **token**.  

To obtain the required credentials, visit https://www.reversinglabs.com/products/file-reputation-service  
Each username can have a certain number of roles for API-s assigned to it. In case your username does not have the required role for your desired action, you will receive an error stating so.  

#### Storing and using the credentials
We will store the credentials in the `credentials.json` file and then load them in our code.

1. Create a JSON file named `credentials.json` in this current folder.
2. Create the following data in that file and replace the placeholder values with your actual username and password:
    ```json
    {
      "ticloud": {
        "username": "your_actual_username",
        "password": "your_actual_password"
      },
      "a1000": {
        "a1000_url": "a1000_url",
        "token": "your_actual_token"
      },
      "tiscale": {
        "tiscale_url": "tiscale_url",
        "token": "your_actual_token"
      }
    }
    ```
3. Save the file.

**NOTE:** The `credentials.json` file must have this exact structure to work.

Instead of doing this step and loading the credentials from the file, 
you can paste your credentials directly into the Python code everytime you create an API object.
