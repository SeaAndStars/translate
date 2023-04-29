# author:SeaStar
# 定义一个调用翻译服务的函数
def translate_text(text, return_language):
    import requests, uuid

    # Add your key and endpoint
    key = "TRANSLATOR_TEXT_SUBSCRIPTION_KEY"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "TRANSLATOR_TEXT_REGION"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': '',
        'to': return_language
        # 'to': ['en', 'ch']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    message = text
    # You can pass more than one object in body.
    body = [{
        'text': message
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    for i in response:
        return i['translations'][0]['text']


while True:
    # 创建一个死循环，让用户可以多次选择翻译语言
    # 选择翻译语言
    language = input("请输入要翻译到的语言(默认为中文\t1 中文2 英文3 日文)\n")
    if language == "1":
        return_language = "zh-Hans"
        break
    elif language == "2":
        return_language = "en"
        break
    elif language == "3":
        return_language = "ja"
        break
    elif language == "":
        return_language = "zh-Hans"
        break
    else:
        print("输入错误，请重新输入")
        continue
# 创建一个死循环调用翻译函数
while True:
    message = input("请输入要翻译的语句(输入stop退出翻译):\n")
    # translate_text(message)
    if message == "stop":
        break
    else:
        # noinspection PyUnboundLocalVariable
        print(translate_text(message, return_language))
# print(response)

# data=json.loads(response) #将字符串转化为Python的列表和字典
# translate_text=data[0]['translations'][0]['text'] #从转化的数据中获取翻译文本
# print(translate_text)

# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
