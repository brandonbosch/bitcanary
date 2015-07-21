# bitcanary

BitCanary is a canary endpoint REST api for service checks status. Instead of treating health pages as a source of truth for overall application health, a canary reports if a service check fails. An HTTP POST tells bitcanary a service is alive and well, and if a service dies, DELETE the canary to notify that the service has failed. A canary can also be used by a load balancer because it returns HTTP success and error codes.

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
