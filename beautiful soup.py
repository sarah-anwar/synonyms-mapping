#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests


# In[7]:


from bs4 import BeautifulSoup


# In[8]:


website = 'https://subslikescript.com/movies'


# In[11]:


result = requests.get(website)
print(result)


# In[15]:


content = result.text
print(content)
soup = BeautifulSoup(content, 'lxml')
print(soup)


# In[17]:


box = soup.find('article', class_ ='main-article')
print(box)


# In[20]:


links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])
print(links)


# In[2]:


from bs4 import BeautifulSoup
import requests
root = 'https://subslikescript.com'  # this is the homepage of the website
website = f'{root}/movies'  # concatenating the homepage with the movies section
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# Locate the box that contains a list of movies
box = soup.find('article', class_='main-article')

# Store each link in "links" list (href doesn't consider root aka "homepage", so we have to concatenate it later)
links = []
for link in box.find_all('a', href=True):  # find_all returns a list
    links.append(link['href'])

for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    # Locate title and transcript
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)


# In[1]:


# Exporting data in a text file with the "title" name
with open(f'{title}.txt', 'w') as file:
        file.write(transcript)


# In[ ]:





# In[ ]:




