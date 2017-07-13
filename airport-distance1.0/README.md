airport-distance1.0

英文项目名称airport-distance1.0，airport代指的是机场的名称，distance代指的是机场之间的里程，1.0指的是第一代
即查询俩个机场之间的里程距离。

# 简介 
输入方面用户可输入想查询里程的两个任意机场的英文名，输出方面则是这两个任意机场间的里程。数据来源于Github用户的资料。
操练Python语言开发练习：使用flask




## 输入：
用户在机场1，机场2，分别输入两个不同的机场英文名。
## 输出：
通过输入两个不同的机场名，用户得到输出结果为：两个机场间的里程
## 从输入到输出，除了flask模块，本组作品使用了：
### 模块
* [csv](https://github.com/Ach3oh/nfu_newmedia_python/blob/master/airport-distance1.0/airport_codes.ipynb)
* [json](https://github.com/Ach3oh/nfu_newmedia_python/blob/master/airport-distance1.0/Untitled.ipynb)
### 数据
* [airport-codes.csv](https://github.com/Ach3oh/nfu_newmedia_python/blob/master/airport-distance1.0/airport-codes.csv)
* [dict.json](https://github.com/Ach3oh/nfu_newmedia_python/blob/master/airport-distance1.0/dict.json)
### API
无
## Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

1. 後端伺服器启动：执行 airport4web.py 启动後端伺服器，等待web 请求。启动成功应出现：  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3. 後端伺服器web 响应：[airport4web.py](airport4web.py) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版[templates/entry.html](templates/entry.html)及两个机场名称（见代码 the_airport1=x,the_airport2=xx,）产出的产生《欢迎来到网上 机场经纬度查询器》的HTML页面

4. 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'x和xx'，使用了HTML5的datalist 定义在 list="airport1、airport2" 及 datalist标签，详见HTML模版[templates/entry.html](templates/entry.html)

5. 前端浏览器web 请求：用户选取指标後按了提交钮「搞吧！」，则产生新的web 请求，按照form元素中定义的method='POST' action='/search4'，以POST为方法，动作为/search4的web 请求

6. 後端服务器收到用户web 请求，匹配到@app.route('/search4', methods=['POST'])的函数 do_search() 

7. [airport4web.py](airport4web.py) 中 def do_search() 函数，把用户提交的数据，以flask 模块request.form['the_user_city']	取到Web 请求中，HTML表单变数名称the_user_city的值，存放在user_city这Python变数下，再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出），其中模版中the_city的值，用user_city这变数之值，其他1项值如此类推。
以flask 模块request.form['input_x''input_xx']	取到Web 请求中，并放到函数的参数中运行得到输出数据，再使用flask模块render_template 函数以templates/results.html模版为基础（输出），其中模版中dista的值，用dista = float(yy1[0]) - float(yy2[0])这变数之值，distb的值，用distb = float(yy1[1]) - float(yy2[1])之值,distaa的值，用distaa = dista * dista这变数之值,distbb的值，用distbb = distb * distb之值, distc 的值，用distc = distaa + distbb)这变数之值,distc1的值，用distc1 = distc ** 0.5之值，distcc = distc1 * 108的值，用distcc = distc1 * 108这变数之值。

8. 前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应，看到输入的两个机场间的里程。

## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)  
Ach3oh    
minxur    
achac   
929384921   
HTGchouse   
xiekunxin   
  
