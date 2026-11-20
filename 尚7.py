import requests
import json

url = "https://jw1.hustwenhua.net/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N2151"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Host": "jw1.hustwenhua.net",
    "Origin": "https://jw1.hustwenhua.net",
    "Referer": "https://jw1.hustwenhua.net/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?gnmkdm=N2151&layout=default",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
}

cookies = {
    "JSESSIONID": "394704C431E922EA739042B714D9C1F2",
    "route": "67e2e44c697c4b936046cc37cb4e27fe"
}

# 注意：这里 xnm、xqm 一定要和抓包里「有效负载」完全一致
data = {
    "xnm": "2026",
    "xqm": "3"
}

resp = requests.post(url, headers=headers, cookies=cookies, data=data)
print("状态码：", resp.status_code)
print("返回片段：", resp.text[:500])

try:
    js = resp.json()
    print("\n✅ JSON 课表数据：")
    print(json.dumps(js, ensure_ascii=False, indent=2))
except Exception as e:
    print("\n❌ JSON 解析失败：", e)

