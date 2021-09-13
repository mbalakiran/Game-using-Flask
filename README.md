# Game-using-Flask
 Simple Game using Flask

## 1 Description 

Write a HTTP-based mini game backend server application that allows users to login, register game scores, and to retrieve a list of high scores for the levels. 

Deliver a zip file containing: 

● A file named “app.py” in the root folder that can be executed with Python 3. ● Additional code in a folder named “src” 

● An optional readme.txt or pdf file with thoughts and considerations about the program Note: This type of exhaustive specification is extremely rare and is only needed based on the circumstances of this test. 

## 2 Nonfunctional requirements 

● The server will be handling a lot of simultaneous requests, so make good use of the available memory and CPU power while not compromising data integrity. 

● Do not use any external frameworks, except if testing is performed. For HTTP, prefer using the http.server Python. 

● The server should run on the port 8080 

● There is no need for persistence storage of data to disk.

● The application should be able to continuously run indefinitely without experiencing a crash or similar. 

## 3Functional requirements 

The endpoints are described in detail below and the notation “<value>” indicates a call parameter value or a return value. 

● If the call is successful, then the HTTP status code 200 should be returned, else the call is unsuccessful and any status code but 200 should be returned. If an appropriate status code is applicable for an unsuccessful call, then return that status code. 

● Numbers, parameters, and return values in the response body are to be in decimal ASCII representation as expected, i.e. not in a binary format. 

● Response data is to be returned as valid JSON objects. 

● Users and levels are created “adhoc”, the first time they are referenced. ● Note the case capitalisation of the request string fields as well as the JSON object property names. 