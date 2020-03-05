# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:19:54 2020

@author: aejimenezg
"""

import src.utilis as utl
import src.analytics as analytics

print(analytics.response_1)

print(analytics.response_2a)
print(analytics.response_2b)

print(analytics.response_3a)
print(analytics.response_3b)
print(analytics.response_3c)


print(analytics.response_4a)
print(analytics.response_4b)
print(analytics.response_4c)
print(analytics.response_4d)

print(analytics.response_5)

print(analytics.response_6a)
print(analytics.response_6b)


utl.export_results(analytics.response_1, "response_1")
utl.export_results(analytics.response_2a, "response_2a")
utl.export_results(analytics.response_2b, "response_2b")
utl.export_results(analytics.response_3a, "response_3a")
utl.export_results(analytics.response_3b, "response_3b")
utl.export_results(analytics.response_3c, "response_3c")
utl.export_results(analytics.response_4a, "response_4a")
utl.export_results(analytics.response_4b, "response_4b")
utl.export_results(analytics.response_4c, "response_4c")
utl.export_results(analytics.response_4d, "response_4d")

utl.export_results(analytics.response_5, "response_5")
utl.export_results(analytics.response_6a, "response_6a")
utl.export_results(analytics.response_6b, "response_6b")
