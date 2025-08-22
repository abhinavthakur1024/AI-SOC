from scripts import elk_integration

def ingest_logs(parsed_logs):
    es = elk_integration.get_client()
    elk_integration.ensure_index(es)
    elk_integration.bulk_index_list(es, parsed_logs)
