#!/usr/bin/python3
"""script reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260
HTTP/1.1" <status code> <file size> (if the format is not
this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption
(CTRL + C), print these statistics from the begining
"""
import sys
import re

statusCode = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
fileSize = 0
counter = 0


def displayStats(dic, fileSize):
    """display stat: status code and numbers of time they appear"""
    print(f"File size:{fileSize}")
    for key in sorted(dic.keys()):
        if statusCode[key] != 0:
            print(f"{key}: {dic[key]}")


if __name__ == "__main__":
    try:
        for val in sys.stdin:
            splitInput = re.split("- |" | "| " " ", str(val))
            statusCodeFileSize = splitInput[-1]
            if counter != 0 and counter % 10 == 0:
                displayStats(statusCode, fileSize)
            counter += 1
            try:
                sCode = int(statusCodeFileSize.split()[0])
                fSize = int(statusCodeFileSize.split()[1])

                if sCode in statusCode:
                    statusCode[sCode] += 1
                fileSize += fSize
            except:
                pass
            displayStats(statusCode, fileSize)
    except KeyboardInterrupt:
        displayStats(statusCode, fileSize)
        raise
