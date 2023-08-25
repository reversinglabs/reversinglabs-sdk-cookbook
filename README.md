# ReversingLabs SDK Cookbook
### A rich and comprehensive knowledge base for the ReversingLabs SDK

The goal of this project is to provide usage examples, configuration hints and to-the-point documentation 
for the **ReversingLabs SDK** (PyPI: https://pypi.org/project/reversinglabs-sdk-py3/, GitHub: https://github.com/reversinglabs/reversinglabs-sdk-py3)

#### Project hierarchy:
- A1000
  - Code examples for using the ReversingLabs SDK A1000 module followed with documentation
- DeepScan
  - Code examples for using the ReversingLabs SDK DeepScan module followed with documentation
- TitaniumCloud
  - Code examples for using the ReversingLabs SDK TitaniumCloud module followed with documentation
- TitaniumScale
  - Code examples for using the ReversingLabs SDK TitaniumScale module followed with documentation

#### How to use the code examples
Code examples are presented in the form of Jupyter Notebooks.  
To use the code from each Jupyter Notebook (.ipynb), the user has two options:
1. Copy the Python code cells (code fragments) into their own script
   - The code cells from one notebook should be copied and joined together into a local Python file
   - After saving the joined code, run the Python file
   - Make sure to copy the imports and put them at the beginning of the Python file
2. Clone the whole project repository locally and run the notebooks
   - Make sure to install the `jupyter` Python package into your development environment (e.g. using pip)
   - Run a local Jupyter server
   - Now you can use the notebook capabilities and execute each code cell separately and see the results

There is also an option to execute the notebooks in a Jupyter server in the cloud but then the package requirements
will need to be also installed into that cloud kernel.