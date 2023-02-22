from flask import Flask


from brownie import *
from solcx import compile_files
import json

def compileSmartContract(contractFileName):

    compilation_directory = "brownie_workspace/build/contracts"
    contracts_directory = "brownie_workspace/contracts/"
    contract_full_path = contracts_directory+contractFileName
    print(contract_full_path)
    compiled_contract = compile_files(contract_full_path)

    contract_name = list(compiled_contract.keys())[0]  # get the name of the contract
    
    contract_interface = compiled_contract[ contract_name ] # get the contract interface. This contains the binary, the abi etc...

    with open(f"{compilation_directory}/{contract_name[len(contract_full_path)+1:]}.json", "w") as output:   # Serialize compiled code to JSON format
        json.dump(compiled_contract, output)

    return contract_interface # get the contract interface. This contains the binary, the abi etc...


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']= "E1O8PJ1ZZ14"

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app