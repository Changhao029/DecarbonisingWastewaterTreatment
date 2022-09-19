
## 1. Data Table API

1. Interface description

First, all data is returned in the form of pages, each page has 200 pieces of data.
Second, query the data by the id and the station name, and return the query result with paginiation.

2. URL

[http://127.0.0.1:50003/datatable/?page=1](http://127.0.0.1:50003/datatable/?page=1)
[http://127.0.0.1:50003/datatable/](http://127.0.0.1:50003/datatable/)
[http://127.0.0.1:50003/datatable/?page=1&id=1](http://127.0.0.1:50003/datatable/?page=1&id=1)
[http://127.0.0.1:50003/datatable/?page=1&id=1&station=231825A](http://127.0.0.1:50003/datatable/?page=1&id=1&station=231825A)

3. HTTP request type

GET request

4. request parameters

There is not any parameter in the request body. However, the query conditions should be in the URL.

5. response field
| field | description | type |  |
| --- | --- | --- | --- |
| count | the number of the response data. | int | 
 |
| next | the next page URL | string |  |
| previous | the previous page URL | string |  |
| results | the response data from the database | list |  |

6. request example

![1663482017687.png](https://cdn.nlark.com/yuque/0/2022/png/25523201/1663482025037-dca38196-eaab-4b0d-83f8-4333e79db865.png#clientId=u29795c5d-d3fb-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=406&id=u4ddf6e4b&margin=%5Bobject%20Object%5D&name=1663482017687.png&originHeight=761&originWidth=1401&originalType=binary&ratio=1&rotation=0&showTitle=false&size=84653&status=error&style=none&taskId=u137d3b73-dabc-4536-96d8-3e33886c764&title=&width=747.2)

7. response example
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "sensor_datetime": "2021-11-30T00:00:30Z",
            "rainfall": null,
            "rainfall_quality": null,
            "temperature": "16.3",
            "temperature_quality": 1,
            "humidity": "88.1",
            "humidity_quality": 147,
            "wind_direction": 274,
            "wind_direction_quality": 1,
            "wind_speed": "6.30",
            "wind_speed_quality": 1,
            "pressure": null,
            "pressure_quality": null,
            "solar_radiation": null,
            "solar_radiation_quality": null,
            "station": "231825A"
        }
    ]
}
```



## 2. Line Chart API

1. Interface description

Return all the data required by the previous line chart.

2. URL

[http://127.0.0.1:50003/linechart/](http://127.0.0.1:50003/linechart/)

3. HTTP request type

GET request

4. request parameters

There is not any parameter in the request body.

5. response field
| field | description | type |  |
| --- | --- | --- | --- |
| station | the station of all the data  | list | 
 |
| sensor_datetime | the sensor datetime of all the data  | list |  |
| temperature | the temperature of all the data  | list |  |
| wind_speed | the wind speed of all the data  | list |  |
| pressure | the  pressure of all the data  | list |  |
| solar_radiation | the solar radiation of all the data  | list |  |

6. request example

![1663484536542.png](https://cdn.nlark.com/yuque/0/2022/png/25523201/1663484542809-633fbac9-50f8-41bb-9edd-365bb3066fed.png#clientId=u29795c5d-d3fb-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=279&id=u00f72a37&margin=%5Bobject%20Object%5D&name=1663484536542.png&originHeight=524&originWidth=1427&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51010&status=error&style=none&taskId=uf5319464-410d-4248-8993-1d4f93d9bf7&title=&width=761.0666666666667)

7. response example
```json
{
  "station":[ 
    "231824A",
    "231828A",
    "231826A",
    "231827A",
    "231825A",
    "231827A",
  ],
  "sensor_datetime": [
    1638230430000.0,
    1638230430000.0,
    1638230430000.0,
    1638230430000.0,
    1638230430000.0,
    1638230460000.0,
  ],
  "temperature": [
    null,
    null,
    "16.5",
    null,
    "16.3",
    null,
  ],
  "wind_speed":[
    "5.67",
    "8.20",
    "9.70",
    "9.10",
    "6.30",
    "8.00",
  ],
  "pressure":[
    null,
    null,
    null,
    null,
    null,
    null,
  ],
  "solar_radiation":[
    "-65.6",
    "-61.6",
    null,
    null,
    null,
    null,
  ],
}
```

## 3. Bar Char API

1. Interface description

Return all the data required by the previous bar chart.

2. URL

[http://127.0.0.1:50003/barchart/](http://127.0.0.1:50003/linechart/)

3. HTTP request type

GET request

4. request parameters

There is not any parameter in the request body.

5. response field
| field | description | type |  |
| --- | --- | --- | --- |
| rainfail | the rainfail of all the data  | list | 
 |
| humidity | the humidity of all the data  | list |  |

6. request example

![1663484501372.png](https://cdn.nlark.com/yuque/0/2022/png/25523201/1663484510758-87a09965-3fcb-4df8-8199-b7554f00937b.png#clientId=u29795c5d-d3fb-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=224&id=u734a3c27&margin=%5Bobject%20Object%5D&name=1663484501372.png&originHeight=420&originWidth=1408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39880&status=error&style=none&taskId=u32c2a6ee-8621-4598-8dae-7bf8fc2d0b7&title=&width=750.9333333333333)

7. response example
```json
{
  "rainfall":[ 
    null,
    null,
    null,
    null,
    null,
    null,
  ],
  "humidity": [
    "88.1",
    "86.3",
    null,
    null,
    "88.5",
    "88.5",
  ],
}
```

## 4. Download API

1. Interface description

Download the data as a CSV file.

2. URL

[http://127.0.0.1:50003/download/?id=1](http://127.0.0.1:50003/download/?id=1)

3. HTTP request type

GET request

4. request parameters

There is not any parameter in the request body. However, the query conditions should be in the URL.

5. response field

The response is a data stream as a HTTP response, and the content type is "text/csv"

6. request example

![1663485562728.png](https://cdn.nlark.com/yuque/0/2022/png/25523201/1663485569017-5ed5be58-d379-49de-a1ed-97509c50c65a.png#clientId=u41f402c9-dd0a-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=197&id=u840db52c&margin=%5Bobject%20Object%5D&name=1663485562728.png&originHeight=370&originWidth=1419&originalType=binary&ratio=1&rotation=0&showTitle=false&size=47139&status=done&style=none&taskId=ub926eb5b-9751-4966-bef8-d30de58062c&title=&width=756.8)

7. response example
```json
id,sensor_datetime,rainfall,rainfall_quality,temperature,temperature_quality,humidity,humidity_quality,wind_direction,wind_direction_quality,wind_speed,wind_speed_quality,pressure,pressure_quality,solar_radiation,solar_radiation_quality,station

1,2021-11-30 00:00:30+00:00,,,16.3,1,88.1,147,274,1,6.30,1,,,,,231825A


```

