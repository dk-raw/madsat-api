# MAD SAT API
Simple API to access data from the [madsat app](https://github.com/dk-raw/madsat)

## Endpoints
- `/events` get events db is CSV format
- `/logs` get process logs
- `/status` get systemctl service status

### Events CSV format
The CSV contains these columns for each event:
| Event ID | Unix Timestamp | Observatory IAGA Code | Observatory Name | Observatory Lat | Observatory Lon | Satellite NORAD ID | Satellite Name | Resolved | Tweet ID |
|----------|----------------|-----------------------|------------------|-----------------|-----------------|--------------------|----------------|----------|----------|

`Resolved` is either `True` or `False` depending on if the event has been resolved, meaning that the correct observatory data have been published, fetched, processed and uploaded to twitter as a reply to the original tweet.

### Logs format
The logs follow this format:
| Log Level | System Time | Message |
|-----------|-------------|---------|
`Log Level` can be `INFO`, `ERROR` or `CRITICAL`. Info logs can be ignored, error logs mean that the app encountered a minor error that does not impact its operation and critical logs indicate major errors that caused the app to fail.

### Status
This endpoint checks the systemctl service to see if the python app runs on my Rasberry Pi 5. `ACTIVE` means that the app is operational and `INACTIVE` means that it is not running.