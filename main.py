
import json
import re

from connector import connect_to_kis_db, fetch_jsons

# Press the green button in the gutter to run the script.
from exporters.aws.aws_opensearch_bulk_exporter import AWSOpenSearchBulkExporter
from providers.bapdb_provider import BAPDBProvider

if __name__ == '__main__':

    db = connect_to_kis_db()
    bapdbs = BAPDBProvider(db).provide()

    bulkexporter = AWSOpenSearchBulkExporter()
    # bulkexporter.create_index()
    bulkexporter.export(bapdbs)

    print('hello')
