import requests
import json


def verify(i, j, r):
    req_json = {
        "device": {"phoneNumber": "+61491578888"},
        "area": {
            "areaType": "Circle",
            "center": {"latitude": -i, "longitude": j},
            "radius": r,
        },
        "maxAge": 120,
    }

    res = requests.post(
        "https://osint-faraday-9e36cbd6acad.2023.ductf.dev/verify",
        data=json.dumps(req_json),
    )
    return res.json()


## step 1
# si, sj = 35, 140
# ti, tj = 40, 150
# DELTA = 1
# i, j = si, sj
# while i < ti:
#     while j < tj:
#         print(i, j)
#         print(verify(i, j, 200000))
#         j += DELTA
#     j = sj
#     i += DELTA

## step 2
# si, sj = 36.2, 146.2
# ti, tj = 37.6, 146.6
# r = 8000
# DELTA = 0.2
# i, j = si, sj
# while i < ti:
#     while j < tj:
#         print(i, j)
#         print(verify(i, j, r))
#         j += DELTA
#     j = sj
#     i += DELTA

## step3
DELTA = 0.01
i, j = 36.44, 146.43
r = 2000
for di in range(-5, 6):
    for dj in range(-5, 6):
        ni, nj = i + di * DELTA, j + dj * DELTA
        print(ni, nj)
        print(verify(ni, nj, r))

"""
{'lastLocationTime': 'Sun Sep  3 03:23:00 2023', 'verificationResult': 'TRUE'}
36.449999999999996 146.42000000000002
{'lastLocationTime': 'Sun Sep  3 03:23:00 2023', 'verificationResult': 'TRUE'}
36.449999999999996 146.43
{'lastLocationTime': 'Sun Sep  3 03:23:00 2023', 'verificationResult': 'TRUE'}
36.449999999999996 146.44
{'lastLocationTime': 'Sun Sep  3 03:23:01 2023', 'verificationResult': 'TRUE'}
36.449999999999996 146.45000000000002
{'lastLocationTime': 'Sun Sep  3 03:23:01 2023', 'verificationResult': 'TRUE'}

36.46 146.42000000000002
{'lastLocationTime': 'Sun Sep  3 03:23:04 2023', 'verificationResult': 'TRUE'}
36.46 146.43
{'lastLocationTime': 'Sun Sep  3 03:23:05 2023', 'verificationResult': 'TRUE'}
36.46 146.44
{'lastLocationTime': 'Sun Sep  3 03:23:05 2023', 'verificationResult': 'TRUE'}
"""
