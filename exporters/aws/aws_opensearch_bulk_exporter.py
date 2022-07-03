import uuid

import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

from exporters.bulk_exporter import BulkExporter


class AWSOpenSearchBulkExporter(BulkExporter):

    def __init__(self):

        host = 'search-tengine2-5nn4xi272rmoglndi7swodwzpy.us-east-1.es.amazonaws.com'
        port = 443
        # auth = ('tengine', '^T3ngine')
        credentials = boto3.Session(
            aws_access_key_id='AKIAUCYMDOCRXMRNIOPV',
            aws_secret_access_key='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',
        ).get_credentials()
        auth = AWSV4SignerAuth(credentials, 'us-east-1')

        self.client = OpenSearch(
            hosts=[{'host': host, 'port': port}],
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

    def create_index(self):
        # Create an index with non-default settings.
        index_name = 'bapdb-reports-tmp-3'
        index_body = {
            'settings': {
                'index': {
                    'number_of_shards': 4
                }
            }
        }

        response = self.client.indices.create(index_name, body=index_body)
        print('\nCreating index:')
        print(response)

    def export(self, data):
        for entry in data:
            # Add a document to the index.
            document = entry.render_json()
            id = str(uuid.uuid4())

            response = self.client.index(
                index='bapdb-reports-prod-7',
                body=document,
                id=id,
                refresh=True
            )

            print('\nAdding document:')
            print(response)



if __name__ == "__main__":
    AWSOpenSearchBulkExporter()