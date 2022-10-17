# Acceptance testing record
local environment: Ubuntu 20.04, Python 3.8, 8GB Memory, 8 CPU

online environment(AWS): S3 bucket, EC2(Ubuntu 20.04, Python 3.8, 2 vCPU, 4GiB Memory)

## Scenario 1

### Scenario name:
Query the data 

### Participating users: 
– Bob – researcher 

### Flow of events: 
– Bob enters the data display page

– Bob inputs the time range, station name or ID of the data he wants to query

– Bob gets the data he wants and click the download button

– Bob gets the data file

### Criteria
1. The data display page can be displayed.
2. The search result is correct according to the query conditions.
3. The search results can be downloaded correctly in the form of a csv file
4. The time to download for three months should be with one and half minutes.

### Result
1. The system can pass all criteria.
2. When the user download the data from 2021/11/30 - 2022/2/28(1.3 million pieces of data), the average time spent is 45s in the local environment. In the online environment(AWS),  the average time spent is 1.3m, which   depends on the performance of the server, the speed of the network, the browser, and so on.
3. The average time to query any data does not exceed five seconds in local environment and online environment.

## Scenario 2

### Scenario name:
View the data visualization

### Participating users: 
– Bob – researcher 

### Flow of events: 
– Bob enters the data visualization page.

– Bob clicks the title of the chart he wants to view and jumps to the chart he wants.

– Bob inputs the time range or station name of the data displayed in this chart.

– Bob gets new chart with the new data.

– Bob clicks the download button to

### Criteria
1. All the charts can be displayed on the data visualization page.
2. All the titles can link to the specific chart.
3. Every chart can display the data correctly that is queried by the user.
4. All charts are loaded within one minute.
5. All the charts can be downloaded as a png picture file.


### Result
1. The system can pass all criteria.
2. The average time for data visualization to load all charts in local environment or online environment is 45s.
3. The average time to download any chart not exceed five seconds in local environment and online environment.





