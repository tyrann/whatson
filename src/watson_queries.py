#!/usr/bin/env python3

import json
from watson_developer_cloud import ToneAnalyzerV3Beta
from credential import USERNAME, PASSWORD


TONE_ANALYZER = ToneAnalyzerV3Beta(
    username=USERNAME,
    password=PASSWORD,
    version='2016-02-11')


def query_watson(string):
    return json.dumps(TONE_ANALYZER.tone(text=string), indent=2)
