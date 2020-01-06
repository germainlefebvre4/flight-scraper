# Flight scraper
## Tags
* [`latest`](https://github.com/germainlefebvre4/flight-scraper/blob/master/Dockerfile), ...

## Quick reference
* **Where to get help:**
   the Docker Community Forums, the Docker Community Slack, or Stack Overflow
* **Where to file issues:**
   https://github.com/germainlefebvre4/flight-scraper/issues
* **Maintained by:**
   [Germain LEFEBVRE](https://github.com/germainlefebvre4)
* **Supported architectures: (more info)**
   amd64
* **Published image artifact details:**
   -
* **Image updates:**
   -
* **Source of this description:**
   [docs repo's dockerhub/ directory (history)](https://github.com/germainlefebvre4/flight-scraper/blob/master/docs/dockerhub/README.md)

## What is Flight Scraper?
### Run the script
```bash
docker run -tid --name=flight-scraper germainlefebvre4/flight-scraper:latest
```

## Parameters
### List of parameters
| Parameter name | Description | Values | Default | Implemented? |
|---|---|---|---|---|
| FLY_ORIGIN | City or airport where you start. | string (IATA code) | 10 | Not yet |
| FLY_DESTINATION | City or airport where you go.  | string (IATA code) | - | Not yet |
| FLY_DATE_DEPARTURE | Date for departure. | string (YYYY-MM-DD) | - | Not yet |
| FLY_DATE_RETURN | Date for return. | string (YYYY-MM-DD) | - | Not yet|

**IATA code is documented at [https://www.iata.org/en/publications/directories/code-search/](https://www.iata.org/en/publications/directories/code-search/) **

### Run the script with parameters
```bash
docker run -tid --name=flight-scraper -e FLY_ORIGIN=CDG -e FLY_DESTINATION=OLB -e FLY_DATE_DEPARTURE=2020-05-09 -e FLY_DATE_RETURN=2020-05-16 germainlefebvre4/flight-scraper:latest
```
