from elasticsearch import Elasticsearch
from config import ES_URL, INDEX

es = Elasticsearch(ES_URL)

mapping = {
    "properties": {
        "route_id":         {"type": "keyword"},
        "trip_id":          {"type": "keyword"},
        "trip_int_id":      {"type": "integer"},
        "route_number":     {"type": "keyword"},
        "route_name":       {"type": "text", "fields": {"raw": {"type": "keyword"}}},
        "short_route_name": {"type": "keyword"},
        "station_name":     {"type": "text", "fields": {"raw": {"type": "keyword"}}},
        "station_code":     {"type": "keyword"},
        "station_int_id":   {"type": "integer"},
        "order_no":         {"type": "integer"},
        "location":         {"type": "geo_point"},
        "fetched_at":       {"type": "date"},
    }
}

if es.indices.exists(index=INDEX):
    print(f"Indeks {INDEX} že obstaja, preskakujem.")
else:
    es.indices.create(index=INDEX, mappings=mapping)
    print(f"Indeks {INDEX} ustvarjen.")