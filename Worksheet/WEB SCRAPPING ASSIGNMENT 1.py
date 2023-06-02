#!/usr/bin/env python
# coding: utf-8

# # ALL THE HEADERS FROM WIKIPEDIA

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get('http://wikipedia.org')

page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


header=[]
for i in soup.find_all('span',class_="other-project-title jsl10n"):
    header.append(i.text)


header


# In[6]:


import pandas as pd
df=pd.DataFrame({'Header':header})
df


# # Q.2 President of india

# In[7]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[8]:


soup=BeautifulSoup(page.content)
soup


# In[9]:


names=[]
for i in soup.find_all('h3',class_=""):
    names.append(i.text)
    
names


# In[10]:


term_of_office=[]
name=soup.find_all('div',class_="presidentListing")
for n in name:
     for m in n.find_all("p"):
            for line in m:
                if not line.text.startswith("T") and not line.text.startswith("h"):
                     term_of_office.append(line)
            
                
                
            
                
term_of_office              


# In[11]:


df=pd.DataFrame({"Name_of_leader":names,"Term_of_office":term_of_office})
df


# # Q.6 JOURNALS ELSEVIER

# In[41]:


urls = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"

#calling url
page = requests.get(urls)
soup = BeautifulSoup(page.content)

#making necessary empty list
paper_title=[]
authors=[]
published_date=[]
paper_url=[]

#Extracting Paper title
Paper_title = soup.find_all("h2", class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")
for i in Paper_title:
    paper_title.append(i.text)
    
#Extracting Authors
Authors = soup.find_all("span", class_="sc-1w3fpd7-0 dnCnAO")
for j in Authors:
    authors.append(j.text)

#Extracting Published date
Published_date = soup.find_all("span", class_="sc-1thf9ly-2 dvggWt")
for k in Published_date:
    published_date.append(k.text)

#Extracting paper urls
Paper_url = soup.find_all("a", class_="sc-5smygv-0 fIXTHm")
for m in Paper_url:
    paper_url.append(m['href'])

#making Dataframe
df = pd.DataFrame({"Paper_Title":paper_title,
                  "Authors":authors,
                  "Published_Date":published_date,
                  "Paper_URL":paper_url})
df


# # Q.5 News details

# In[20]:


page10=requests.get('https://www.cnbc.com/world/?region=world')
page10


# In[42]:


headlines=soup.find_all("span",class_="Latest News")
len(headlines)
for i in range(len(headlines)):
    print(headlines[i].text)


# In[ ]:


data_cnbc=pd.DataFrame(headlines)
data_cnbc.to_csv("https://www.cnbc.com/world/?region=world.csv",index=True)


# In[19]:


url='https://www.cnbc.com/world/?region=world'
r=requests.get(url)
soup2=BeautifulSoup(r.text,'lxml')
print("First four href links from the webpage cnbc.com:")
print(soup.find_all('a'))


# In[ ]:





# # Q.3Cricket ranking

# In[37]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[ ]:





# In[39]:


soup1=BeautifulSoup(page.content)
soup1


# In[ ]:





# In[ ]:


#top 10 team


# In[40]:


team=soup1.find_all("span",class_="u-hide-phablet")
team_name=[]
for i in team:
    team_name.append(i.text)
matches=[]
points=[]
rating=[]
new_list=[]

for i in soup1.find_all("td",class_="rankings-block__banner--matches"):
    matches.append(i.text)
for i in soup1.find_all("td",class_="rankings-block__banner--points"):
    points.append(i.text)
for i in soup1.find_all("td",class_="rankings-block__banner--rating u-text-right"):
    rating.append(i.text)
for i in soup1.find_all("td",class_="table-body__cell u-center-text"):
    new_list.append(i.text)
for i in range(0,len(new_list)-1,2):
    matches.append(new_list[i])
    points.append(new_list[i+1])
for i in soup1.find_all("td",class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
    
    
    
    
df1=pd.DataFrame({})
df1["Team_name"]=team_name[:10]
df1["Matches"]=matches[:10]
df1["Points"]=points[:10]
df1["Rating"]=rating[:10]
df1


# In[ ]:


#top 10 batsmen


# In[35]:


page1=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page1


# In[ ]:





# In[36]:


soup2=BeautifulSoup(page1.content)
players=[]
team_name=[]
rating=[]
for i in soup2.find_all("div",class_="rankings-block__banner--name-large"):
    players.append(i.text)
for i in soup2.find_all("div",class_="rankings-block__banner--nationality"):
    team_name.append(i.text.replace("\n",""))
for i in soup2.find_all("div",class_="rankings-block__banner--rating"):
    rating.append(i.text)
    
for i in soup2.find_all("td",class_="table-body__cell rankings-table__name name"):
    for j in i.find_all("a"):
         players.append(j.text)
for i in soup2.find_all("span",class_="table-body__logo-text"):
    team_name.append(i.text)
for i in soup2.find_all("td",class_="table-body__cell rating"):
    rating.append(i.text)
    
df2=pd.DataFrame({})
df2["Players"]=players[:10]
df2["Team_name"]=team_name[:10]
df2["Rating"]=rating[:10]
df2


# In[ ]:


#10 top bowler


# In[33]:


page3= requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page3


# In[ ]:





# In[34]:


soup3=BeautifulSoup(page3.content)
players=[]
team_name=[]
rating=[]
for i in soup3.find_all("div",class_="rankings-block__banner--name-large"):
    players.append(i.text)
for i in soup3.find_all("div",class_="rankings-block__banner--nationality"):
    team_name.append(i.text)
for i in soup3.find_all("div",class_="rankings-block__banner--rating"):
    rating.append(i.text)
    
for i in soup3.find_all("td",class_="table-body__cell rankings-table__name name"):
    for j in i.find_all("a"):
        players.append(j.text)
for i in soup3.find_all("span",class_="table-body__logo-text"):
    team_name.append(i.text)
for i in soup3.find_all("td",class_="table-body__cell rating"):
    rating.append(i.text)
    
df3=pd.DataFrame({})
df3["Players"]=players[:10]
df3["Team_name"]=team_name[0:10]
df3["Rating"]=rating[0:10]
df3


# In[ ]:


#Q.4 dataframe for women cricket team


# In[31]:


page4=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page4


# In[ ]:





# In[32]:


soup5=BeautifulSoup(page4.content)
women_team=soup5.find_all("span",class_="u-hide-phablet")
women_team_name=[]
for i in women_team:
    women_team_name.append(i.text)
women_matches=[]
women_points=[]
women_ratings=[]
women_new_list=[]
for i in soup5.find_all("td",class_="rankings-block__banner--matches"):
    women_matches.append(i.text)
for i in soup5.find_all("td",class_="rankings-block__banner--points"):
    women_points.append(i.text)
for i in soup5.find_all("td",class_="rankings-block__banner--rating u-text-right"):
    women_ratings.append(i.text)
for i in soup5.find_all("td",class_="table-body__cell u-center-text"):
    women_new_list.append(i.text)
    for i in range(0,len(women_new_list)-1,2):
        women_matches.append(women_new_list[i])
        women_points.append(women_new_list[i+1])
for i in soup5.find_all("td",class_="table-body__cell u-text-right rating"):
    women_ratings.append(i.text)
    
df5=pd.DataFrame({})
df5["Team_name"]=women_team_name[0:10]

df5["Matches"]=women_matches[0:10]

df5["points"]=women_points[0:10]
df5["Rating"]=women_ratings[0:10]
df5


# In[ ]:





# In[ ]:


#top 10 women players


# In[29]:


page5=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
page5


# In[ ]:





# In[30]:


soup6=BeautifulSoup(page5.content)
players=[]
team_name=[]
rating=[]
for i in soup6.find_all("div",class_="rankings-block__banner--name-large"):
    players.append(i.text)
for i in soup6.find_all("div",class_="rankings-block__banner--nationality"):
    team_name.append(i.text)
for i in soup6.find_all("div",class_="rankings-block__banner--rating"):
    rating.append(i.text)
    
for i in soup6.find_all("td",class_="table-body__cell rankings-table__name name"):
    for j in i.find_all("a"):
        players.append(j.text)
for i in soup6.find_all("span",class_="table-body__logo-text"):
    team_name.append(i.text)
for i in soup6.find_all("td",class_="table-body__cell rating"):
    rating.append(i.text)
    
df6=pd.DataFrame({})
df6["Players"]=players[:10]
df6["Team_name"]=team_name[:10]
df6["Rating"]=rating[:10]
df6


# In[ ]:





# In[ ]:


#top 10 women allrounder


# In[ ]:


page6=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
page6


# In[ ]:


soup7=BeautifulSoup(page6.content)
player=[]
team=[]
rating=[]
for i in soup7.find_all("div",class_="rankings-block__banner--name-large"):
    player.append(i.text)
for i in soup7.find_all("div",class_="rankings-block__banner--nationality"):
    team.append(i.text)
for i in soup7.find_all("div",class_="rankings-block__banner--rating"):
    rating.append(i.text)
    
for i in soup7.find_all("td",class_="table-body__cell rankings-table__name name"):
    for j in i.find_all("a"):
        player.append(i.text)
for i in soup7.find_all("span",class_="table-body__logo-text"):
    team.append(i.text)
for i in soup7.find_all("td",class_="table-body__cell rating"):
    rating.append(i.text)
    
df7=pd.DataFrame({})
df7["Player"]=player[:10]
df7["Team"]=team[:10]
df7["rating"]=rating[:10]
df7


# # Q.7 Details from dineout
# 

# In[27]:


page8=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page8


# In[ ]:





# In[28]:


soup8=BeautifulSoup(page8.content)
name=[]
location=[]
cuisine=[]
rating=[]
images=[]
for i in soup8.find_all("div",class_="restnt-info cursor"):
    name.append(i.text)
for i in soup8.find_all("div",class_="restnt-loc ellipsis"):
    location.append(i.text)
for i in soup8.find_all("span",class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])
for i in soup8.find_all("div",class_="restnt-rating rating-4"):
    rating.append(i.text)
for i in soup8.find_all("img",class_="no-img"):
    images.append(i.get('data-src'))
df8=pd.DataFrame({})
df8["Name"]=name
df8["Location"]=location
df8["Cuisine"]=cuisine
df8["rating"]=rating
df8["Images"]=images
df8


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




