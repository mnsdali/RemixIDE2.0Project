import subprocess



contract_file_name = "votingDaliMMA"
def compile_smart_contract(contract_name):
    # Change the working directory to the directory where the smart contract is located
     
    working_directory = f"../brownie_workspace/contracts/"
    cmd = f"brownie compile {contract_name}.sol"

    # Use the subprocess module to execute the command
    process = subprocess.Popen(cmd, cwd=working_directory, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(stdout.decode())


from brownie import *
from solcx import compile_files
import json

def compileSmartContract(contractFileName):

    compilation_directory = "../brownie_workspace/build/contracts"
    contracts_directory = "../brownie_workspace/contracts/"
    contract_full_path = contracts_directory+contractFileName+".sol"
    compiled_contract = compile_files(contract_full_path)

    contract_name = list(compiled_contract.keys())[0]  # get the name of the contract
    
    contract_interface = compiled_contract[ contract_name ] # get the contract interface. This contains the binary, the abi etc...

    with open(f"{compilation_directory}/{contract_name[len(contract_full_path)+1:]}.json", "w") as output:   # Serialize compiled code to JSON format
        json.dump(compiled_contract, output)

    return contract_interface # get the contract interface. This contains the binary, the abi etc...
    


print(compileSmartContract(contract_file_name)['abi'])

"""
my_project = project.load("../brownie_workspace")




def compile_solidity_file(file_path):
    with open(file_path, 'r') as file:
        solidity_code = file.read()
    compiled_code = solcx.compile_source(solidity_code)
    
    return compiled_code['<stdin>:Voting']['abi']



print(compile_solidity_file(f'../brownie_workspace/contracts/voting.sol'))

# Load the Brownie project

from brownie import *

project = project.load("../brownie_workspace")  # Load the contract


# Compile the contract
project.compile_contracts()

# Get the compiled bytecode and ABI
bytecode = MyContract._build["bytecode"]
abi = MyContract.abi


contract_name = "test"
contract = (f'{brownieProjectPath}/contracts/{contract_name}.sol', "0.8.1" )[contract_name]
#
print('ABI:', contract.abi)
print('Bytecode:', contract.bytecode)

if os.path.exists(f'{brownieProjectPath}/contracts/{contract_name}.sol'):
    print("The path exists.")
else:
    print("The path does not exist.")"""