import requests
from bs4 import BeautifulSoup
import pandas as pd



page = requests.get("https://forecast.weather.gov/MapClick.php?lat=25.8215&lon=-80.332#.YcSF8SxOn0o")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id='seven-day-forecast-list')
forecast_items = seven_day.find_all(class_="forecast-tombstone")
tonight = forecast_items[0]
print(tonight.prettify())


period_tags = seven_day.select(".forecast-tombstone .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".forecast-tombstone  .short-desc")]
temps = [t.get_text() for t in seven_day.select(".forecast-tombstone  .temp")]
descs = [d["title"] for d in seven_day.select(".forecast-tombstone  img")]
print(short_descs)
print(temps)
print(descs)


weather = pd.DataFrame({
    "period": periods,
    "short_descs": short_descs,
    "temps": temps,
    "descs": descs
})

print(weather)