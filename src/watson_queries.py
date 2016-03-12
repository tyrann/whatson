#!/usr/bin/env python3

from watson_developer_cloud import ToneAnalyzerV3Beta
from credential import WATSON_USERNAME, WATSON_PASSWORD

TONE_ANALYZER = ToneAnalyzerV3Beta(
    username=WATSON_USERNAME,
    password=WATSON_PASSWORD,
    version='2016-02-11')

def query_watson(string):
    return TONE_ANALYZER.tone(text=string)
