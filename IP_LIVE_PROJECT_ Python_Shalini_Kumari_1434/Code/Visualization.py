#!/usr/bin/env python
# coding: utf-8

# In[99]:


#importing all required files
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
get_ipython().run_line_magic('matplotlib', 'inline')

import plotly
import plotly.express as px
import plotly.graph_objects as go
plt.rcParams['figure.figsize']=17,8
import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot
from plotly.offline import iplot

import folium


# In[41]:


pyo.init_notebook_mode(connected=True)
cf.go_offline()


# In[100]:


#defining dataframes by using CollegeList.csv


# In[62]:


df=pd.read_csv(r"C:\Users\shalini\Desktop\Live Project\ScrappingCode\CollegeList.csv")


# In[4]:


df


# In[43]:


print('Total number colleges in list are '+str(len(df.index)))


# In[6]:


df


# In[ ]:


#importing Natural Language Toolkit
#NLTK is a leading platform for building Python programs to work with human language data.it guides the reader through the fundamentals of writing Python programs,
#working with corpora, categorizing text, analyzing linguistic structure, and more.


# In[44]:


import nltk
nltk.download('punkt')


# In[45]:


import re
import math
from collections import defaultdict
from nltk.probability import FreqDist
from nltk.tokenize.api import TokenizerI


# In[ ]:


#displaying information about number of colleges per city


# In[46]:


top_N = 29
a = df['Location'].str.cat(sep=' ')
words = nltk.tokenize.word_tokenize(a)
word_dist = nltk.FreqDist(words)
print (word_dist)


# In[ ]:





# In[47]:


Numberofcollegepercity = pd.DataFrame(word_dist.most_common(top_N),
                    columns=['CityName', 'NumberofColleges'])


# In[48]:


Numberofcollegepercity


# In[79]:


Numberofcollegepercity.style.background_gradient(cmap='Blues')


# In[101]:


Numberofcollegepercity.iplot(kind='bar',
         x='CityName',
         y='NumberofColleges',
         xTitle='Name of City in Maharashtra',
         yTitle='Number of Colleges',
         title='Bar Graph - Number of Colleges per City',
         color='blue'
        )


# In[102]:


Numberofcollegepercity.iplot(kind='scatter',
         x='CityName',
         y='NumberofColleges',
         mode='markers+lines',
         xTitle='Name of City in Maharashtra',
         yTitle='Number of Colleges',
         title='Line Graph - Number of Colleges per City',
         colors='blue',
         size=20   
        )


# In[103]:


import matplotlib.pyplot as plt
import pandas as pd

city_data = Numberofcollegepercity["CityName"]
college_data = Numberofcollegepercity["NumberofColleges"] 
plt.pie(college_data, labels=city_data,radius=1.5,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart - Number of Colleges per City")
plt.show()


# In[ ]:





# In[ ]:


#displaying information about affiliated colleges


# In[63]:


top_N = 17
b = df['AffiliatedTo'].str.cat(sep=' ')
words = nltk.tokenize.word_tokenize(b)
word_dist = nltk.FreqDist(words)
print (word_dist)


# In[104]:


AffiliatedColleges = pd.DataFrame(word_dist.most_common(top_N),
                    columns=['AffiliatedUniversity', 'NumberofColleges'])


# In[67]:


AffiliatedColleges


# In[105]:


AffiliatedColleges.style.background_gradient(cmap='Greens')


# In[106]:


AffiliatedColleges.iplot(kind='bar',
         x='AffiliatedUniversity',
         y='NumberofColleges',
         xTitle='Universities in Maharashtra',
         yTitle='Number of Colleges',
         title='Bar Graph - Number of Affiliated Universties',
         color='green'                
         
        )


# In[107]:


AffiliatedColleges.iplot(kind='scatter',
         x='AffiliatedUniversity',
         y='NumberofColleges',
         mode='markers+lines',
         xTitle='Name of City in Maharashtra',
         yTitle='Number of Colleges',
         title='Line Graph - Number of Affiliated Universties',
         colors='green',
         size=20   
        )


# In[98]:


import matplotlib.pyplot as plt
import pandas as pd

city_data = AffiliatedColleges["AffiliatedUniversity"]
college_data = AffiliatedColleges["NumberofColleges"] 
plt.pie(college_data, labels=city_data,radius=2.8,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart - Number of Affiliated Universties")
plt.show()

