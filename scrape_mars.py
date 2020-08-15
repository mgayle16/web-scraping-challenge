#!/usr/bin/env python
# coding: utf-8

# In[1]:

#dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time


# In[5]:


# get_ipython().system('which chromedriver')


# In[6]:


#pointing to the directory where chromedriver exists
executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless = False)


# # NASA Mars News

# In[7]:


#launch website
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[8]:


#write to html file using bS
html = browser.html
soup = bs(html,"html.parser")


# In[11]:


news_title = soup.find("div",class_="content_title").text
# news_info_paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
# print(f"Para: {news_info_paragraph}")


# # JPL Mars Space Images - Featured Image

# In[12]:


featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(featured_image_url)


# In[14]:


#Gather base url
from urllib.parse import urlsplit
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(featured_image_url))
print(base_url)


# In[28]:


#Selector code used to grab the image
xpath = "//*[@id=\"full_image\"]"


# In[29]:


#Full Res. image using splinter to click on the mars featured image
results = browser.find_by_xpath(xpath)
img = results[0]
img.click()


# In[31]:


#get image url
html_image = browser.html
soup = bs(html_image, "html.parser")
img_url = soup.find("img", class_="fancybox-image")["src"]
full_res_img_url = base_url + img_url
print(full_res_img_url)


# # Mars Weather

# In[32]:


#get mars weather's latest tweet from the website
mars_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(mars_weather)


# In[51]:


twitter_weather = browser.html
soup = bs(twitter_weather, "html.parser")
mars_weather_twitter = soup.find("div", class_="css-1dbjc4n r-156q2ks").text
print(mars_weather_twitter)


# # Mars Facts

# In[52]:


mars_facts_url = "https://space-facts.com/mars/"


# In[55]:


#pull table info using table tag from the webiste 
table = pd.read_html(mars_facts_url)
table[0]


# In[57]:


mars_facts_df = table[0]
mars_facts_df.columns = ["Parameters", "Values"]
mars_facts_df.set_index(["Parameters"])


# In[62]:


mars_facts_html_table = mars_facts_df.to_html()
mars_facts_html_table = mars_facts_html_table.replace("\n", "")
print(mars_facts_html_table)


# # Mars Hemispheres

# In[63]:


hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemisphere_url)


# In[65]:


##Gather base url
hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(hemisphere_url))
print(hemisphere_base_url)


# In[85]:


hemisphere_urls = []
results = browser.find_by_xpath( "//*[@id=\"product-section\"]/div[2]/div[1]/div/a/h3").click()
time.sleep(2)
cerberus_open = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
time.sleep(1)
cerberus_image = browser.html
soup = bs(cerberus_image, "html.parser")
cerberus_url = soup.find("img", class_="wide-image")["src"]
cerberus_img_url = hemisphere_base_url + cerberus_url
print(cerberus_img_url)
cerberus_title = soup.find("h2",class_="title").text
print(cerberus_title)
cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
hemisphere_urls.append(cerberus)
back_button = browser.visit(hemisphere_url)


#click back button browser before running next line


# In[88]:


results1 = browser.find_by_xpath( "//*[@id=\"product-section\"]/div[2]/div[2]/div/a").click()
time.sleep(2)
schiaparelli_open = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
time.sleep(1)
schiaparelli_image = browser.html
soup = bs(schiaparelli_image, "html.parser")
schiaparelli_url = soup.find("img", class_="wide-image")["src"]
schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
print(schiaparelli_img_url)
schiaparelli_title = soup.find("h2",class_="title").text
print(schiaparelli_title)
schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
hemisphere_urls.append(schiaparelli)
back_button = browser.visit(hemisphere_url)


# In[92]:


results1 = browser.find_by_xpath( "//*[@id=\"product-section\"]/div[2]/div[3]/div/a").click()
time.sleep(2)
syrtis_major_open = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
time.sleep(1)
syrtis_major_image = browser.html
soup = bs(syrtis_major_image, "html.parser")
syrtis_major_url = soup.find("img", class_="wide-image")["src"]
syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
print(syrtis_major_img_url)
syrtis_major_title = soup.find("h2",class_="title").text
print(syrtis_major_title)
syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
hemisphere_urls.append(syrtis_major)
back_button = browser.visit(hemisphere_url)


# In[96]:


results1 = browser.find_by_xpath( "//*[@id=\"product-section\"]/div[2]/div[4]/div/a").click()
time.sleep(2)
valles_marineris_open = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
time.sleep(1)
valles_marineris_image = browser.html
soup = bs(valles_marineris_image, "html.parser")
valles_marineris_url = soup.find("img", class_="wide-image")["src"]
valles_marineris_img_url = hemisphere_base_url + valles_marineris_url
print(valles_marineris_img_url)
valles_marineris_title = soup.find("h2",class_="title").text
print(valles_marineris_title)
valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
hemisphere_urls.append(valles_marineris)
back_button = browser.visit(hemisphere_url)


# In[97]:


hemisphere_urls


# In[ ]:




