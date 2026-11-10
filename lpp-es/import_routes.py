import time
import requests
from datetime import datetime, timezone
from elasticsearch import Elasticsearch, helpers
from config import ES_URL, API_BASE, INDEX, HEADERS, REQUEST_DELAY

es = Elasticsearch(ES_URL)


def get_json(path, params=None):
    r = requests.get(f"{API_BASE}{path}", params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    body = r.json()
    if not body.get("success", False):
        raise RuntimeError(f"API napaka: {body}")
    return body["data"]


def build_actions(route, stations, now):
    for s in stations:
        yield {
            "_index": INDEX,
            "_id": f"{route['trip_id']}_{s['order_no']}",
            "_source": {
                "route_id": route["route_id"],
                "trip_id": route["trip_id"],
                "trip_int_id": route["trip_int_id"],
                "route_number": route["route_number"],
                "route_name": route["route_name"],
                "short_route_name": route["short_route_name"],
                "station_name": s["name"],
                "station_code": s["station_code"],
                "station_int_id": s["station_int_id"],
                "order_no": s["order_no"],
                "location": {"lat": s["latitude"], "lon": s["longitude"]},
                "fetched_at": now,
            },
        }


def main():
    now = datetime.now(timezone.utc).isoformat()

    routes = get_json("/route/routes")
    print(f"Najdenih tripov: {len(routes)}")

    total_docs = 0
    for i, route in enumerate(routes, 1):
        try:
            stations = get_json("/route/stations-on-route", {"trip-id": route["trip_id"]})
        except Exception as e:
            print(f"[{i}/{len(routes)}] NAPAKA {route['route_number']} {route['trip_id']}: {e}")
            continue

        if not stations:
            print(f"[{i}/{len(routes)}] {route['route_number']}: prazno, preskakujem")
            continue

        ok, _ = helpers.bulk(es, build_actions(route, stations, now))
        total_docs += ok
        print(f"[{i}/{len(routes)}] {route['route_number']} {route['route_name']}: {ok} postaj")
        time.sleep(REQUEST_DELAY)

    print(f"Končano. Skupaj indeksiranih dokumentov: {total_docs}")


if __name__ == "__main__":
    main()