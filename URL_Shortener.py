#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

# The original URL that you want to shorten
url = "https://www.example.com/"

# TinyURL API endpoint
api_url = "http://tinyurl.com/api-create.php?url="

# Make a request to TinyURL API
short_url = requests.get(api_url + url).text

print(f"Original URL: {url}")
print(f"Shortened URL: {short_url}")

