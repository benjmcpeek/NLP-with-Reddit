import pandas as pd
import requests
import time
import datetime


def get_reddit_data(subreddit, filt):
    
    client_id = input('client_id:')
    client_secret = input('client_secret:')
    user_agent = input('user_agent:')
    username = input('username:')
    password = input('password:')

    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

    data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    
    headers = {'User-Agent': 'Ben_McPeek/0.0.1'}

    res = requests.post(
        'https://www.reddit.com/api/v1/access_token',
        auth=auth,
        data=data,
        headers=headers)

    print(res)
    res.json()
    token = res.json()['access_token']
    headers['Authorization'] = f'bearer {token}'

    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).status_code == 200
    
    
    base_url = 'https://oauth.reddit.com/r/'

    res = requests.get(base_url+subreddit+filt, headers=headers)
    
    
    
    results = []
    params = {
        'limit': 100,
    }
    for i in range(1, 11):
        res = requests.get(base_url+subreddit,
                           headers=headers,
                          params=params)
        data = res.json()

        for i in range(len(data['data']['children'])):
            new_submission = {}
            new_submission['title'] = data['data']['children'][i]['data']['title']
            new_submission['text'] = data['data']['children'][i]['data']['selftext']
            new_submission['subreddit'] = data['data']['children'][i]['data']['subreddit']
            new_submission['name'] = data['data']['children'][i]['data']['name']
            if new_submission['title'] not in results:
                results.append(new_submission)

        params['after'] = results[-1]['name']
        print(params)
        time = str(datetime.datetime.now())
        print(f'Time of Request: {time[0:-7]}, Amount of Posts: {len(results)}')
        
    first_subs = pd.DataFrame(results) 
    first_subs.to_csv(f'../data/{subreddit}.csv', mode='a', index=False)
    
    
    
    
    
    


    


