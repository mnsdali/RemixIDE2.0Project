from flask import Flask


from brownie import *
from solcx import compile_files
import subprocess
import json

def brownieCompile(contractFileName):
    # Change the working directory to the directory where the smart contract is located
     
    working_directory = f"./brownie_workspace/contracts/"
    cmd = f"brownie compile {contractFileName}"

    # Use the subprocess module to execute the command
    process = subprocess.Popen(cmd, cwd=working_directory, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

def compileSmartContract(contractFileName):

    compilation_directory = "brownie_workspace/build/contracts"
    contracts_directory = "brownie_workspace/contracts/"
    contract_full_path = contracts_directory+contractFileName
    print(contract_full_path)
    compiled_contract = compile_files(contract_full_path)

    contract_name = list(compiled_contract.keys())[0]  # get the name of the contract
    
    contract_interface = compiled_contract[ contract_name ] # get the contract interface. This contains the binary, the abi etc...

    # with open(f"{compilation_directory}/{contract_name[len(contract_full_path)+1:]}.json", "w") as output:   # Serialize compiled code to JSON format
        # json.dump(compiled_contract, output)

    #return [contracts_directory,contractFileName,  contract_name[len(contract_full_path)+1:]] # get the contract interface. This contains the binary, the abi etc...
    return  contract_name[len(contract_full_path)+1:] #return the artifact name

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SECRET_KEY']= "E1O8PJ1ZZ14"

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app