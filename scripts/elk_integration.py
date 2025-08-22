# scripts/elk_integration.py

from elasticsearch import Elasticsearch, helpers
from datetime import datetime
import logging

# Elasticsearch index name
INDEX_NAME = "syslog_data"

# Define index mappings
MAPPINGS = {
    "mappings": {
        "properties": {
            "host": {"type": "keyword"},
            "action": {"type": "keyword"},
            "message": {"type": "text"},
            "dest_ip": {"type": "ip"},
            "pid": {"type": "integer"},
            "@timestamp": {"type": "date"}  # ✅ Added timestamp field
        }
    }
}

def get_client():
    """
    Connect to Elasticsearch.
    Assumes ES is running locally on default port (9200).
    """
    es = Elasticsearch("http://localhost:9200")
    return es


def ensure_index(es, index=INDEX_NAME):
    """
    Ensure index exists with mappings.
    If not, create it.
    """
    if not es.indices.exists(index=index):
        es.indices.create(index=index, body=MAPPINGS)
        logging.info(f"Created index '{index}'")


def bulk_index_list(es, data_list, index=INDEX_NAME):
    """
    Bulk ingest a list of documents into Elasticsearch.
    Adds @timestamp to each doc.
    """
    actions = [
        {
            "_index": index,
            "_source": {
                **doc,
                "@timestamp": datetime.utcnow().isoformat()  # ✅ add timestamp
            }
        }
        for doc in data_list
    ]

    helpers.bulk(es, actions)
    logging.info(f"Ingested {len(data_list)} documents to '{index}'")
