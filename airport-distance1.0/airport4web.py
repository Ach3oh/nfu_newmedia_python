 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from airport import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('airport.log', 'a', encoding='utf8') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['airport1']
    letters = request.form['airport2']
    	
    title = '以下是您的结果：'
    results = search4letters(airport1, airport2)
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_airport1=airport1,
                           the_airport2=airport2,
                           the_results=results,
                        
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上 机场距离查询器')


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
