import re
import pandas as pd
f=open('WhatsApp Chat with IT 2nd Yr - B(2022-23) (1).txt' , 'r',encoding='utf-8')
data=f.read()
print(data)
# pattern
pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
messages = re.split(pattern, data)[1:]
len(messages)
dates = re.findall(pattern, data)
dates
df = pd.DataFrame({'user_message':messages, 'message_date': dates})
df['message_date'] = pd.to_datetime(df['message_date'], format='%d%m%Y, %H:%M - ')
df.rename(columns={'message_date': 'date'}, inplace=True)
df.head()
users = []
messages = []
for message in df['user_message']:
    entry = re.split('([\w\W]+?):\s', message)
    if entry[1:]:
        users.append(entry[1])
        messages.append(entry[2])
    else:
        users.append('group_notification')
        messages.append(entry[0])
df['users'] =  users
df['message'] = messages
df.drop(columns=['user_message'], inplace=True)

df.head()
df['year'] = df['date'].dt.year
df.head()
df['month'] = df['date'].dt.month_name()
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
df.head()
d

