from flask import Flask, render_template, request
import config
import post

def page_not_found(e):
      return render_template('404.html'), 404

## 初始化：导入Flask库，定义Flask实例化对象
## Flask实例化时，需要传入__name__:目的是接收包或者模块的名字作为参数
app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

## 定义一个应用方法，并且route装饰器装饰
## 调用route()方法装饰创建的应用方法：目的是告诉flask怎么访问该函数

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['blogTopic']
            blogT = post.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.replace('\n', '<br>')

        if 'form2' in request.form:
            prompt = request.form['blogSection']
            blogT = post.generateBlogSections(prompt)
            blogSectionIdeas = blogT.replace('\n', '<br>')

        if 'form3' in request.form:
            prompt = request.form['blogExpander']
            blogT = post.blogSectionExpander(prompt)
            blogExpanded = blogT.replace('\n', '<br>')


    return render_template('index.html', **locals())

## 在main中，flask实例化对象调用run()方法，进行运行
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
