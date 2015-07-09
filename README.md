# bitcanary

BitCanary is a REST API for service healthchecks. Instead of treating health pages as a source of truth for overall application health, it's a simple tool to help diagnose where a failure occured. An HTTP POST tells bitcanary a service is alive and well, and if a service dies, the monitor app can HTTP DELETE the canary to notify that the service has failed its health check.

## Examples
Make a new canary endpoint
```
curl -i -H "Content-Type: application/json" -X POST -d '{"canary": "wowza"}' http://localhost:5000/canary
```
Get the status of all your canaries
```
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/canary
```

This will return something like:

```
{
  "canaries": [
    {
      "canary": "BitCanary", 
      "description": "BitCanary status", 
      "status": true, 
      "uri": "http://localhost:5000/canary/1"
    }, 
    {
      "description": "", 
      "status": true, 
      "title": "wowza", 
      "uri": "http://localhost:5000/canary/3"
    }
  ]
}
```

A service health check fails, and you want to mark the canary as dead with a DELETE:
```
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/canary/2
```
