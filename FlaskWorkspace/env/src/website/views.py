import os
from flask import Blueprint, render_template, request, session, flash
from brownie import Contract, network, project
from website import compileSmartContract




#define a blueprint
views = Blueprint('views', __name__)

#decorator
@views.route('/')
def home():
    return render_template("base.html")



@views.route('/submit-form', methods=["GET","POST"])
def submit_form():
    if request.method == 'POST':
        contract_name = request.form.get('file')
        if contract_name == '':
            flash('You need to choose a smart contract before procceeding!', category="error")
            return render_template("base.html")
        
        if 'compileBtn' in request.form:
            # Compile a specific contract
            current_path = os.getcwd()
            print("Current path:", current_path, "**********************************************")
            session['contractName'] = contract_name
            compiled_contract = compileSmartContract(session['contractName'])
            session['contractJSON'] = compiled_contract
            flash("the smart contract has been compiled successfully and is ready for deployment!", category="success")
            # Compile a specific contract
            return render_template("base.html")
        
        elif 'deployBtn' in request.form:
            if  'contractJSON' not in session.keys():
                flash("you need to compile the smart contract before deployment", category="error")
            else:
                flash("the smart contract has been deployed successfully", category="success")
                # more code ...

            return render_template("deployed.html")
    else:
        return render_template("base.html")

    

