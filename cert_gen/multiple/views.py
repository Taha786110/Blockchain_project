from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import details_csv,civil_details,comp_details,mech_details,elec_details
from home.models import details
from .resources import detailscsvresource
from django.contrib import messages
from tablib import Dataset
import csv,io
import pandas as pd
import numpy as np
import json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import date

from web3 import Web3

# In the video, we forget to `install_solc`
# from solcx import compile_standard
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware

load_dotenv()
# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/')
def multiple(request):
    # return HttpResponse("This is Homepage ")
    if request.method == 'POST':
        # details_resource = detailscsvresource()
        # dataset = Dataset()
        # new_details = request.FILES['myfile']

        # data_set = new_details.read().decode('UTF-8')
        # io_string = io.StringIO(data_set)
        # next(io_string)
        # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        #     created = details_csv.objects.update_or_create(
        #         id=column[0],
        #         name=column[1],
        #         program=column[2],
        #         year=column[3],
        #         tx_rc = column[4])
        df = pd.read_csv('./myfile.csv')
        nd = df.to_numpy()
        ln = len(nd)
        for i in range(ln):
            arr = nd[i]
            id = str(arr[0])
            name = str(arr[1])
            program = str(arr[2])
            year = str(arr[3])
            yr = str(arr[4])
            sem = str(arr[5])
            grade = str(arr[6])
            department = str(arr[7])
            start_date = str(arr[8])
            end_date = str(arr[9])
            with open("./certification.sol", "r") as file:
                certification_file = file.read()

            # We add these two lines that we forgot from the video!
            install_solc("0.8.0")

            # Solidity source code
            compiled_sol = compile_standard(
                {
                    "language": "Solidity",
                    "sources": {"certification.sol": {"content": certification_file}},
                    "settings": {
                        "outputSelection": {
                            "*": {
                                "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                            }
                        }
                    },
                },
                solc_version="0.8.0",
            )

            with open("compiled_code.json", "w") as file:
                json.dump(compiled_sol, file)
                

            # with open('./Certification.json', 'r') as file:
            #     compiled_sol = file.read()


            # get bytecode
            bytecode = compiled_sol["contracts"]["certification.sol"]["Certification"]["evm"]["bytecode"]["object"]

            # get abi
            abi = json.loads(compiled_sol["contracts"]["certification.sol"]["Certification"]["metadata"])["output"]["abi"]

            w3 = Web3(Web3.HTTPProvider("{Your Infura API}"))
            chain_id = {Your testnet Chain ID}

            if chain_id == 4:
                w3.middleware_onion.inject(geth_poa_middleware, layer=0)
                print(w3.clientVersion)
            #Added print statement to ensure connection suceeded as per
            #https://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority

            my_address = "{Your wallet address}"
            private_key = "{Your Wallet Private key}"


            Certification = w3.eth.contract(abi=abi, bytecode=bytecode)

            # Get the latest transaction
            nonce = w3.eth.get_transaction_count(my_address)
            # Submit the transaction that deploys the contract
            transaction = Certification.constructor().build_transaction(
                {
                    "chainId": chain_id,
                    "gasPrice": w3.eth.gas_price,
                    "from": my_address,
                    "nonce": nonce,
                }
            )


            # Sign the transaction
            signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
            # Send it!
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            # Wait for the transaction to be mined, and get the transaction receipt
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            tx_rc = tx_receipt.contractAddress


            cert = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

            store_transaction = cert.functions.generateCertificate(id,name,program,year).build_transaction(
                {
                    "chainId": chain_id,
                    "gasPrice": w3.eth.gas_price,
                    "from": my_address,
                    "nonce": nonce + 1,
                }
            )


            signed_store_txn = w3.eth.account.sign_transaction(
                store_transaction, private_key=private_key
            )


            tx_store_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_store_hash)
            img = Image.open('cert.jpg')

            # Call draw Method to add 2D graphics in an image
            I1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype("Arial.ttf",size=30)
            today = date.today()
            tod_str = str(today)
            # Add Text to an image
            I1.text((754, 320), name, fill=(0, 0, 0), font=myFont)
            I1.text((550, 380), program, fill=(0, 0, 0), font=myFont)
            I1.text((570, 490), year, fill=(0, 0, 0), font=myFont)
            I1.text((70, 580), tx_rc, fill=(0, 0, 0), font=myFont)


            
            # Display edited image
            img.show()
            
            # Save the edited image
            img.save(f"cert{i}.png")
            username = request.user.username
            if username == 'comp':
                Details = comp_details(name=name, verify_id=id, program=program, year=year,tx_rc=tx_rc,yr=yr, sem = sem, grade = grade, Department = department, start_date=start_date,end_date=end_date)
                Details.save()
                messages.success(request, "details Saved.")
            elif username == 'civil':
                Details = civil_details(name=name, verify_id=id, program=program, year=year,tx_rc=tx_rc,yr=yr, sem = sem, grade = grade, Department = department, start_date=start_date,end_date=end_date)
                Details.save()
                messages.success(request, "details Saved.")
            elif username == 'mech':
                Details = mech_details(name=name, verify_id=id, program=program, year=year,tx_rc=tx_rc,yr=yr, sem = sem, grade = grade, Department = department, start_date=start_date,end_date=end_date)
                Details.save()
                messages.success(request, "details Saved.")
            elif username == 'elec':
                Details = elec_details(name=name, verify_id=id, program=program, year=year,tx_rc=tx_rc,yr=yr, sem = sem, grade = grade, Department = department, start_date=start_date,end_date=end_date)
                Details.save()
                messages.success(request, "details Saved.")
    return render(request, 'multiple.html')


# def verification(request):
#     return render(request, 'verification.html')
