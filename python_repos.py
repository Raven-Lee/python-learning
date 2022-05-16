import requests

# call api and save the respond
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# save respond data in a variable
respond_dict = r.json()

# handle it
print("Total repositories: ",respond_dict['total_count'])

repo_dicts = respond_dict['items']
print("repositories returned:", len(respond_dict))

repo_dict = repo_dicts[0]

print('\nSelected information about first repository:')
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])