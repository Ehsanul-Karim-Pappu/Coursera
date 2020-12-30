import requests
username = 'ehsan3p'
token = '5ddeefc3351788fca7ba5f85f8f0c52259a2bc6f'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content.decode())
else:
    print('Got unexpected status code {}: {!r}'.format(
        response.status_code, response.content))
