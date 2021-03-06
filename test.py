#!/usr/bin/env python
import json
import sys

import requests


d = {
    "streams": [
        {
            "subsite": "TEST",
            "node": "TEST",
            "sensor": "TEST",
            "method": "streamed",
            "stream": "ctdbp_no_sample",
            "parameters": [3651]
        }
    ],
    "coefficients": {
        "CC_a0": 1.0,
        "CC_a1": 1.0,
        "CC_a2": 1.0,
        "CC_a3": 1.0,
        "CC_lat": 1.0,
        "CC_lon": 1.0
    },
    # "start": 3634042590.2004886,
    #    "stop": 3634043605.3394685
    "start": 1,
    "stop": 10
}

d2 = {
    "streams": [
        {
            "subsite": "XX00XXXX",
            "node": "XX00X",
            "sensor": "00-CTDPFW100",
            "method": "recovered",
            "stream": "ctdpf_ckl_wfp_instrument_recovered",
            "parameters": [1959]
        }
    ]
}

d3 = {
    "streams": [
        {
            "subsite": "RS00ENGC",
            "node": "XX00X",
            "sensor": "00-ADCPSK002",
            "method": "streamed",
            "stream": "adcp_pd0_beam_parsed",
            "parameters": []
        }
    ],
    "coefficients": {
        "CC_lat": 1.0,
        "CC_lon": 1.0
    },
}

d4 = {
    "streams": [
        {
            "subsite": "RS00ENGC",
            "node": "XX00X",
            "sensor": "00-CTDPFA002",
            "method": "streamed",
            "stream": "ctdpf_sbe43_sample",
            "parameters": [908, 909, 910, 911, 912]
        },
        {
            "subsite": "RS00ENGC",
            "node": "XX00X",
            "sensor": "00-ADCPSK002",
            "method": "streamed",
            "stream": "adcp_pd0_beam_parsed",
            "parameters": []
        }
    ],
    "coefficients": {
        "CC_lat": 1.0,
        "CC_lon": 1.0
    },
}

d5 = {
    "streams": [
        {
            "subsite": "RS00ENGC",
            "node": "XX00X",
            "sensor": "00-VELPTD002",
            "method": "streamed",
            "stream": "velpt_velocity_data",
            "parameters": [3230, 3231, 3232]
        }
    ],
    "coefficients": {
        "CC_lat": 1.0,
        "CC_lon": 1.0
    },
    "start": 3634051000.0,
    "stop": 36340513000.0
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post('http://localhost:5000/netcdf', data=json.dumps(d5), headers=headers, stream=True)
for chunk in r.iter_content(100):
    sys.stdout.write(chunk)
    sys.stdout.flush()
