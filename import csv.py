import csv
import argparse
import requests

parser = argparse.ArgumentParser()                                               
parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument("--env", "-e", type=str, required=True)
parser.add_argument("--token", "-t", type=str, required=True)
args = parser.parse_args()

def downloadFile(correspondent_id,env,token,client_document_id,filename):
    headers = {
        'accept': 'application/octet-stream',
        'Authorization': token,
    }
    request_String = "https://{}-api.{}.apexcrypto.com/apex-crypto/api/v2/documents/{}".format(correspondent_id,env,client_document_id)
    response = requests.get(
        request_String,
        headers=headers,
    )
    with open(filename, 'wb') as f:
        f.write(response.content)

with open(args.file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        correspondent_id = row['correspondent_id']
        client_document_id = row['client_document_id']
        external_id = row['external_id']
        type_id = row['type']
        content_type = row['content_type']
        document_type = row['document_type']
        description = row['description']

        if document_type == 'RAW_CIP_DATA':
            content_type =".json"
        else:
            content_type =".jpeg"

        filename = "{}_{}_{}_{}_{}{}".format(correspondent_id,external_id,client_document_id,document_type,description,content_type)
        downloadFile(correspondent_id, args.env, args.token, client_document_id, filename)
        print (filename)