# ReversingLabs SDK Cookbook
### A rich and comprehensive knowledge base for the ReversingLabs SDK

The goal of this project is to provide usage examples, configuration hints and to-the-point documentation 
for the **ReversingLabs SDK**.

#### Project hierarchy:
The whole project is separated into the following module directories:
- A1000
  - Code examples for using the ReversingLabs SDK A1000 module followed with documentation
- DeepScan
  - Code examples for using the ReversingLabs SDK DeepScan module followed with documentation
- TitaniumCloud
  - Code examples for using the ReversingLabs SDK TitaniumCloud module followed with documentation
- TitaniumScale
  - Code examples for using the ReversingLabs SDK TitaniumScale module followed with documentation

Each module directory has its own readme instructions for creating the required Python objects, using the credentials and covering any other important configuration actions.

 ---

#### Installing the ReversingLabs SDK
The ReversingLabs SDK is available on the **Python Package Index (PyPI)**: https://pypi.org/project/reversinglabs-sdk-py3/  
To install it, run the following command using **pip** in your console/terminal:

`pip install reversinglabs-sdk-py3`

This will install the ReversingLabs SDK into your current Python interpreter.

##### Additional info:
The GitHub repository with the latest source code is available at: https://github.com/reversinglabs/reversinglabs-sdk-py3

 ---
    
#### How to use the code examples
Code examples are presented in the form of Jupyter Notebooks.  
To use the code from each Jupyter Notebook (.ipynb), the user has three options:
1. Copy the Python code cells (code fragments) into their own script
   - The code cells from one notebook should be copied and joined together into a local Python file
   - After saving the joined code, run the Python file
   - Make sure to copy the imports and put them at the beginning of the Python file
2. Clone the whole project repository locally and run the notebooks
   - Make sure to install the `jupyter` Python package into your development environment (e.g. using pip)
   - Run a local Jupyter server
   - Now you can use the notebook capabilities and execute each code cell separately and see the results
3. Run the Python script files with the same name as the corresponding Jupyter notebook
   - Example: To run all the code from the `file_reputation_and_analysis.ipynb` notebook, run the `file_reputation_and_analysis.py` file using `python file_reputation_and_analysis.py`
   - The Python script files contain only Python code and can also be run using an editor of your choice. The editor needs to have a configured Python interpreter with the ReversingLabs SDK installed 

There is also an option to execute the notebooks in a Jupyter server in the cloud but then the package requirements
will need to be also installed into that cloud kernel.