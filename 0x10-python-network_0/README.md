# Python - Network #0

Project done during Full Stack Software Engineering studies at **ALX AFRICA SE School**. In this networking project, I used `curl` in Bash scripts to send various types
of HTTP headers. In the process, I learned about how URL's work, domain names,
the many different HTTP request/repsonse header fields and status codes, and
how to utilize cookies.

Task six was an algorithm challenge separate from the overall project theme
completed in Python.

*****

## Tests :heavy_check_mark:

* [tests](./tests): This directory contains all my test files for this project.

## Table of contents
Files | Description
----- | -----------
[0-body_size.sh](./0-body_size.sh) | Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
[1-body.sh](./1-body.sh) | Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
[2-delete.sh](./2-delete.sh) | Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
[3-methods.sh](./3-methods.sh) | Bash script that takes in a URL and displays all HTTP methods the server will accept
[4-header.sh](./4-header.sh) | Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
[5-post_params.sh](./5-post_params.sh) | Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
[6-peak.py](./6-peak.py) | Python function that finds a peak in a list of unsorted integers
[6-peak.txt](./6-peak.txt) | Time complexity of the algorithm used in 6-peak.py
[100-status_code.sh](./100-status_code.sh) | Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response
[101-post_json.sh](./101-post_json.sh) | Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
[102-catch_me.sh](./102-catch_me.sh) | Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response

*****

## Tasks :page_with_curl:

NOTE: The `curl` behavior in all Bash scripts were written to interact with a
server set up on a container.

* **0. cURL body size**
  [0-body_size.sh](./0-body_size.sh): Bash script that sends a `GET` request to
  a given URL and displays the size of the response body in bytes.

* **1. cURL to the end**
  * [1-body.sh](./1-body.sh): Bash script that sends a `GET` request to a given
  URL and displays the response body for a `200` status code response.

* **2. cURL Method**
  * [2-delete.sh](./2-delete.sh): Bash script that sends a `DELETE` request to
  a given URL and displays the response body.

* **3. cURL only methods**
  * [3-methods.sh](./3-methods.sh): Bash script that displays all HTTP methods
  the server of a given URL will accept.

* **4. cURL headers**
  * [4-header.sh](./4-header.sh): Bash script that sends a `GET` request to a
  given URL with a header variable `X-HolbertonSchool-User-Id=98` and displays
  the response body.

* **5. cURL POST parameters**
  * [5-post_params.sh](./5-post_params.sh): Bash script that sends a `POST`
  request to a given URL with the variables `email=test.gmail.com` and
  `subject=I will always be here for PLD` and displays the response body.

* **6. Find a peak**
  * [6-peak.py](./6-peak.py): [Technical interview preparation] - Python
  program that finds a peak in a list of unsorted integers.
  * [6-peak.txt](./6-peak.txt): Text file containing the complexity of the
  algorithm.

* **7. Only status code**
  * [100-status_code.sh](./100-status_code.sh): Bash script that sends a `GET`
  request to a given URL without using pipes, redirections, `;`, or `&&` and
  displays the status code of the response.

* **8. cURL a JSON file**
  * [101-post_json.sh](./101-post_json.sh): Bash script that sends a JSON `POST`
  request with the contents of a provided file to a given URL, and displays the
  response body.

* **9. Catch me if you can!**
  * [102-catch_me.sh](./102-catch_me.sh): Bash script that sends a request to
  `0.0.0.0:5000/catch_me` that causes the server to respond with a message
  containing `You got me!` in the repsonse body.


## Autor

```Success Chikezie```

### Connect me!

<div>

<a  href="https://twitter.com/succynice"  target="_blank">  <img  align="left"  alt="Success Chikezie | Twitter"  src="https://img.shields.io/twitter/follow/succynice?style=social"/>  </a>

<a  href="https://www.linkedin.com/in/succynice/"  target="_blank">  <img  align="left"  alt="Success Chikezie | LinkedIn"  src="https://img.shields.io/badge/LinkedIn-+24K-blue?style=social&logo=linkedin"/>  </a>

<a  href="https://github.com/succynice/"  target="_blank">  <img  align="left"  src="https://img.shields.io/github/followers/succynice?style=social"  alt="Ralex | Github">  </a>
</br>
</div>
