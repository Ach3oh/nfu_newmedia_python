<!doctype html>
<html lang="zh-CN" >
    <head>
        <title>{{ the_title }}</title>
    </head>
    <body>

<h2>{{ 欢迎各用户的使用，让我们开始挑选喜欢的游戏吧！！！}}</h2>

<form method='POST' action='/search4'>
<br>
<br>
<tr><td>电子邮箱 </td><td><input type="email" name="user_email" /></td></tr>
<tr><td>密码: </td><td><input type="password" name="user_password" /></td></tr>
<p>性别：</p>
<input type="radio" name="sex" value="male" checked>男
<br>
<input type="radio" name="sex" value="female">女
<br>
<tr><td>steam评分: </td><td><input type="range" name="range" min="1" max="10" /></td></tr>
<tr><td>上映日期: </td><td><input type="date" name="date" /></td></tr>
<br>
<p>游戏类型：</p>
<input type="radio" name="games type" value="funny" checked>有趣
<br>
<input type="radio" name="games type" value="adventure" >冒险
<br>
<input type="radio" name="games type" value="fansasy" >幻想
<br>
<input type="radio" name="games type" value="mystery" >悬念
<br>
<input type="radio" name="games type" value="thriller" >惊悚

</table>
<p>准备就绪后, 单击此按钮：</p>
<p><input value='搞吧！' type='SUBMIT'></p>
</form>

   </body>
</html>