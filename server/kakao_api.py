import requests\nimport os\nfrom dotenv import load_dotenv\n\nload_dotenv()\n\nKAKAO_API_TOKEN = os.getenv('KAKAO_API_TOKEN')\n\ndef send_message(chat_id, message):\n    url = f\
https://api.kakao.com/v1/messages/send\\n    headers = {\n        \Authorization\: f\Bearer
KAKAO_API_TOKEN
\,\n        \Content-Type\: \application/json\\n    }\n    data = {\n        \chat_id\: chat_id,\n        \message\: message\n    }\n    response = requests.post(url, headers=headers, json=data)\n    return response.json()\n
