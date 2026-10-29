# Ljubljana Student Housing & Commute Index
Ljubljana Student Housing & Commute Index je spletna aplikacija z interaktivnim zemljevidom, namenjena študentom v Ljubljani. Aplikacija omogoča enostavno iskanje in izbiro študentskih domov na podlagi časa potovanja z mestnim avtobusom (LPP) do izbranega fakultetnega središča ter vpogled v stroške bivanja.

## 💡 Glavne funkcionalnosti
Izbira fakultete (POI):
Uporabnik izbere svojo fakulteto v Ljubljani (npr. FRI, FKKT, EF, FDV, FMF ...).
Izbrana fakulteta se na zemljevidu jasno označi s posebno ikono.

### Time-to-Faculty Heatmap:

Na podlagi potovanja z LPP avtobusom se okoli izbrane fakultete dinamično izrišejo 3 barvne časovne cone (izohrone):

🟢 Zeleno območje: Do 15 minut vožnje.

🟡 Rumeno območje: 15–30 minut vožnje.

🟠 Oranžno območje: 30–45 minut vožnje.

### Sloj študentskih domov in stroškov (Dormitories & Cost Layer):

Prikaz izbranih lokacij študentskih domov (ŠDL) na zemljevidu.
Ob kliku na dom se prikaže pop-up okno z podrobnostmi: naziv doma, ocenjen čas potovanja do izbrane fakultete ter mesečna cena bivanja.

## 🛠 Tehnološki sklad (Tech Stack)
### Baza podatkov & Analitika:
Elasticsearch: Shranjevanje, indeksiranje in geo-prostorsko poizvedovanje (Geo-queries) po lokacijah fakultet, študentskih domov ter avtobusnih linij in voznih redov.
Kibana: Vizualizacija, upravljanje indeksov ter spremljanje in analitika geo-podatkov.

Backend:
Python (FastAPI) ali Node.js za komunikacijo med frontendom in Elasticsearch bazo.

Frontend:
HTML/JS (ali React) z uporabo Leaflet.js / MapLibre GL JS za prikaz interaktivnega zemljevida in izris barvnih poligonov.

## 📁 Podatkovni viri
Fakultete in študentski domovi: Vnaprej pripravljeni geografski podatki (koordinati in cene bivanja) shranjeni v Elasticsearch.
LPP linije in vozni redi: Podatki o trasah ter časih potovanja z mestnimi avtobusi LPP.

## 🚀 Možnosti razvoja
- Dodajanje ostalih načinov prevoza (peš, kolo / BicikeLJ, avtomobil).

- Integracija LPP API-ja v realnem času za analizo zanesljivosti in zamud avtobusov preko Kibana nadzornih plošč.

- Dodatni sloji študentskega življenja (lokacije s ponudbo na študentske bone, trgovine, knjižnice).