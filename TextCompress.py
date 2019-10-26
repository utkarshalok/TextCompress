import csv
import re


# In[129]:


'''user_string= " he is good C M R .He is a good C M "
res=re.findall(r'(?:(?<=\s|\s)[A-Z]\s)+',user_string)
res
l=[]
for i in res:
    print(i.split())
    print("".join(i.split()))
    l.append("".join(i.split()))
l

res = re.findall(r'(?:(?<=\s|\s)[A-Z]\s)+', test_string) 


# In[5]:


res = re.findall(r'(?:(?<=\s|\s)[A-Z]\s)+', user_string) 
len(res)


# In[23]:


user_string= "i have two dollars please give it to one in need triple A . Praful Naik is a good C M .U S S  disintegrated into parts end"
res = re.findall(r'(?:(?<=\s|\.)[A-Z]\s)+',user_string) 
res


# In[24]:


user_string= "i have two dollars please give it to one in need triple A . Praful Naik is a good C M .U S S  disintegrated into parts end"
'''
def text_compress(user_string):
    res = re.findall(r'(?:(?<=\s|\.)[A-Z]\s)+',user_string) 
    l=[]
    #print(res)
    for i in res:
        i=i.strip()
        l.append("".join(i.split()))
    #print(l)
    for i in range(len(res)):
        user_string = user_string.replace(res[i],l[i])
        
    #print("After subs----",user_string)   
    _str = user_string.split(' ')
    #print(len(_str))
    for i in range(len(_str)-1):
    # File path which consists of Abbreviations.
      fileName = "ruleBook.txt"
      # File Access mode [Read Mode]
      accessMode = "r"
      with open(fileName, accessMode) as myCSVfile:
      # Reading file as CSV with delimiter as "=", so that abbreviation are stored in row[0] and phrases in row[1]
        dataFromFile = csv.reader(myCSVfile, delimiter="=")
        #print(len(_str[i]))
        for row in dataFromFile:

            if row[0]==_str[i]:
                #print(i)
                if _str[i+1]=='dollar':
                    _str[i]='$'+row[1]
                    _str[i+1]='del flag'
                    i=i+1
                if _str[i+1]=='dollars':
                    flag=_str[i]
                    _str[i]='$'+row[1]
                    _str[i+1]='del flag'
                    i=i+1
                if len(_str[i+1])==1:
                    _str[i]=eval(row[1])
                    _str[i+1]='del flag'
                    #print("ii",i)
                    i+=1
                
    print(' '.join(_str[i] for i in range(len(_str)-1) if _str[i]!='del flag'))
        



while True:
    print("Please write the text")
    user = input()
    if user == 'end':
        print("Ending Thanks for Using")
        break
    text_compress(user)




