# Follow this steps to start collect data

## 1. CREDENTIAL set up for API request
1. open file "CREDENTIAL"  
2. put your access token in the 1st line of "CREDENTIAL" file  
3. put your ad id in the 2nd line of the "CREDENTIAL" file  

## 2. Read "get_audience_data.py"
1. This file contain the logic for making API requests  
2. The comments are the description of how the script work  
3. Read the comments to understand the procedures  
4. If you are confused how each function work, take a look at the "request_lib.py" file specific details.  

## 3. How it works: 
## (read along with the get_audience_data.py file)  
1. Before request: **"get_audience_data.py" line 1-36**
We are about to make a GET request which is acquiring resources from a remote server.  
We need to have:
  1. verification: our CREDENTIAL  
  2. specification: the parameters (country, age, gender, ids...)  
  3. encoding for the url  

2. Making requests: **"get_audience_data.py" line 38-43**
We use our constructed url to make GET request with the 
function called "api_request()".
This function requries 4 inputs:
  1. the **url_list** returned by build_url() function  
  2. the **url_list's start position** (starts at 0, but may change because the request is stopped due to request rate limit reached)  
  3. the **country name** we are about to make request with  
  4. the **user group id** we are about to make request to obtain the group audience size for our studied user group  

This function returns 3 outputs:
  1. the **the processed api response** contains the country name, gender, age group, dau, mau, and group id  
  2. the **the end position of interrupted request** due to limit reached for saving checkpoint for restarting at the right place  
  3. the **flag variable** to check if the rate limit is reached  

3. Writing responses: **"get_audience_data.py" line 46-47**
Results will be writed to the file called "api_responses.csv" using appending mode to append new responses to the file.  

4. Checkpoint for limit reach insurance:  **"get_audience_data.py" line 49-56**
This part of the code is used for saving checkpoint when the limit is reach.  
After the program terminated due to limit reach, you can continue to the exact spot of the start of the unfinished request lists.  

## 4. Start collecting data
0. run `python toy.py` to understand the queries FIRST!  
1. run `python get_audience_data.py`  
2. possible improvements:  
  1. create a loop to the outest level of the main() function to create random pause for never reaching the limit specified in the "check_request_limit()" function  
3. feel free to conduct experiments with different ideas