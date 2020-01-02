from flask import Flask, url_for, redirect, request
from urllib.parse import urlparse, urljoin


app = Flask(__name__)


@app.route('/hello')
def hello():
    return "hello"


@app.route('/page1')
def page1():
    return '<h1>Page1 Page</h1><a href="%s">Do Something</a>' % url_for('do_something', next=request.full_path)


@app.route('/page2')
def page2():
    return '<h1>Page2 Page</h1><a href="%s">Do Something</a>' % url_for('do_something', next=request.full_path)


@app.route('/do_something')
def do_something():
    return redirect_back()


# 判断上一个页面的方式：
#   1. 根据referrer判断，但是referrer容易被修改，删除。也可能为空；
#   2. 在URL中手动加入包含当前页面URL的查询参数，一般设置为next；
#   3. 如果都没有找到，设置一个默认值。
def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
        return redirect(url_for(default, **kwargs))


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    # scheme：网络协议    netloc：服务器位置（用户信息）
    # print(test_url.scheme, "    ", test_url.netloc)
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
