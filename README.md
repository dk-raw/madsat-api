# MAD SAT API
Simple Flask API to access data from the [madsat app](https://github.com/dk-raw/madsat)

## Endpoints
- `/events` get events db in JSON or CSV format
- `/logs` get logs
- `/status` get systemctl service status

### Events
You can request all the events in the database in either JSON or CSV format. By default the API returns the JSON data. If you want the CSV converted data, add `format=csv` (case sensistive) on the request url as a query parameter.

An event is a satellite passage above a selected magnetometer station.

An event is considered resolved when the data from the magneotmeter station have been published, downloaded by the app then processed for anomalies and uploaded to Twitter as a graph.

#### Events JSON format
The JSON follows this structure
```JSON
{
    "_id": {
        "$oid": "unique event ID string"
    },
    "timestamp": unix timestamp Double,
    "obsIAGA": "observatory three letter IAGA code",
    "obsName": "observatory common name",
    "obsLat": observatory latitude Double,
    "obsLon": "observatory longtitude Double,
    "satNORAD": "satellite NORAD ID",
    "satName": "satellite common name",
    "tweetID": "tweet ID String",
    "resolved": resolution status Boolean
}
```

#### Events CSV format
The CSV contains these columns for each event:
| Event ID | Unix Timestamp | Observatory IAGA Code | Observatory Name | Observatory Lat | Observatory Lon | Satellite NORAD ID | Satellite Name | Tweet ID | Resolution status |
|----------|----------------|-----------------------|------------------|-----------------|-----------------|--------------------|----------------|----------|----------|

### Logs format
The logs follow this format:
| Log Level | System Time | Message |
|-----------|-------------|---------|

`Log Level` can be `INFO`, `ERROR` or `CRITICAL`. Info logs can be ignored, error logs mean that the app encountered a minor error that does not impact its operation and critical logs indicate major errors that caused the app to fail.

Currently `System Time` is on my local timezone, Athens UTC+02:00 or UTC+03:00 according to Eastern European Time.

### Status
This endpoint checks the systemctl service status and returns `ACTIVE` or `INACTIVE`.

> [!IMPORTANT]  
> The API is hosted locally on the same Rasberry Pi 5 as the MAD SAT app so if the API isn't accessible, chances are neither is the app.