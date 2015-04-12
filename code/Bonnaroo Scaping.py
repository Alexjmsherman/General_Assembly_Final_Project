# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:19:50 2015

@author: alsherman
"""
import requests
from bs4 import BeautifulSoup

#get line up page on bonnaroo website
url = r'http://lineup.bonnaroo.com/'
response = requests.get(url)
c = response.content
soup = BeautifulSoup(c)

#find all band names 
a = soup.find_all('a', 'band')
a = soup.find_all('a')

for band in a:
    print band
   
 <div class="fl-pop-actions">
            <span>9699 Bonnaroo fans<br>added this artist.</span>
              <a href="/band/45112/fans/toggle" class="fl-add ds-add-remove">Add to Line-up</a>  </div>