 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from airport import search4letters
import json
app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('airport.log', 'a', encoding='utf8') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    x = request.form['airport1']
    xx = request.form['airport2']
    
    with open('dict.json','r') as file:
     r = json.load(file)

    y1 = r[x]
    y2 = r[xx]
    yy1 = y1.split(',')
    yy2 = y2.split(',')
    dista = float(yy1[0]) - float(yy2[0])
    distb = float(yy1[1]) - float(yy2[1])
    distaa = dista * dista
    distbb = distb * distb
    distc = distaa + distbb
    distc1 = distc ** 0.5
    distcc = distc1 * 108
    
    title = '以下是您的结果：'
   
    return render_template('results.html',
                           the_title=title,
                           the_airport1=x,
                           the_airport2=xx,
                           the_y1=y1,
                           the_distcc=distcc
                          )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上 机场经纬度查询器')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('airport.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('表单内容', '访问者IP', '浏览器', '运行结果')
    return render_template('viewlog.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
