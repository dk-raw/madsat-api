# MAD SAT API
Simple Flask API to access data from the [madsat app](https://github.com/dk-raw/madsat)

## Endpoints
- `/events` get events db in JSON or CSV format
- `/logs` get logs
- `/status` get systemctl service status

### Events
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

`Resolved` is either `True` or `False` depending on if the event has been resolved, meaning that the correct observatory data have been published, fetched, processed and uploaded to twitter as a reply to the original tweet.

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