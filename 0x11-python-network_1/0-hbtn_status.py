#!/usr/bin/python3
"""script that fetches 'https://alx-intranet.hbtn.io/status' """

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') \
            as response:
        htmlContent = response.read()
    print("Body response:")
    print('\t- type: {}'.format(type(htmlContent)))
    print('\t- content: {}'.format(htmlContent))
    print('\t- utf8 content: {}'.format(htmlContent.decode('UTF-8')))
