import os
import sys, json
import subprocess
from flask import Blueprint, render_template, request, session, flash
from brownie import *
from website import compileSmartContract, brownieCompile
from eth_account import Account



#define a blueprint
views = Blueprint('views', __name__)

# Modify the `autocompile` setting



#requirements to work with brownie project
brownie_path = "./brownie_workspace"
brownieName = "brownieWS"
proj = project.load(brownie_path, name=brownieName)

scripts_path = os.path.join(brownie_path, 'scripts')
##########

#decorator
@views.route('/')
def home():
    return render_template("base.html")



@views.route('/submit-form', methods=["GET","POST"])
def submit_form():
    if request.method == 'POST':
        contract_name = request.form.get('fileName')
        
        if contract_name == '':
            flash('You need to choose a smart contract before procceeding!', category="error")
            return render_template("base.html")
        file= request.files['file']
        
        if 'compileBtn' in request.form:
            #################### version 1
            # Compile a specific contract
            #current_path = os.getcwd()
            #print("Current path:", current_path, "**********************************************")
            # session['contractsPath'],session['fileName'], session['contractName'] = compiled_contract
            
            file.save(os.path.join(brownie_path+"/contracts", contract_name))
            
            compiledContractName = compileSmartContract(contract_name)
            brownieCompile(contract_name)
            session['contractName'] = compiledContractName
            
            abi = json.dumps(proj._build.get(compiledContractName)['abi'])
            loaded_abi= json.loads(abi)
            
            flash("the smart contract has been compiled successfully and is ready for deployment!", category="success")
            return render_template("compile.html", session=session, abi=loaded_abi)
        
        elif 'deployBtn' in request.form:
            
            if not request.form.get('contractName'):
                flash("you need to compile the smart contract before deployment", category="error")
            else:
                
                contractName = request.form.get("contractName")
                abi = proj._build.get(contractName)['abi']
                
                #fetch constructor input from post request
                constructorInputs = []
                for query in abi:
                    if query['type'] == 'constructor':
                        for inp in query['inputs']:
                            if '[]' in inp['type']:
                                arr = request.form.get(inp['name']).split(',')

                                if 'bytes' in inp['type']:
                                    arr = map(lambda data : data.strip().encode('utf-8'),arr)
                                elif 'int' in inp['type']:
                                    arr = map(lambda data : int(data), arr)
                                elif 'fixed' in inp['type']:
                                    arr = map(lambda data : float(data), arr) 

                                constructorInputs.append(arr)
                            else:
                                elem = inp['type']
                                if 'bytes' in elem:
                                    elem = elem.strip()
                                elif 'int' in inp['type']:
                                    elem = int(elem)
                                elif 'fixed' in inp['type']:
                                    elem = float(elem)
                                constructorInputs.append(elem)

                # deploy with brownie

                
                
                
                #fileName = request.form.get("fileName")
                # get the contract object using the contract name as a string
                #load the brownie project
                # print(project.get_loaded_projects())
                # print("##########")
                
                #create instance for our contract
                #contractContainer = Contract.from_abi(contractName, contractName, proj._build.get(compiledContractName)['abi'] )

                
                
                #deploy the contract on local ganache of brownie
                #deployedContract = contractContainer.deploy({'from' : accounts[0]})
                
                
                flash("the smart contract has been deployed successfully", category="success")
                # more code ...
                accounts= [Account.create() for i in range(10)]
                for account in accounts:
                    print(account.address)
            return render_template("deployed.html")
        elif 'backBtn' in request.form:
            return  render_template("base.html")
    else:
        return render_template("base.html")

    

