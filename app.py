from flask import Flask
from flask import render_template

app = Flask(__name__)
posts = [
    {
        'author':'tharun',
        'title':'blog 1',
        'date': '22-02-2022',
        'body':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse augue purus, viverra ornare erat at, suscipit vestibulum enim. Duis auctor ex vitae venenatis placerat. Ut egestas felis vitae velit tristique facilisis. Sed id augue placerat, sollicitudin tellus eu, interdum lacus. Cras rhoncus nulla ac fermentum blandit. Nulla a tincidunt dui. Morbi blandit ipsum ultricies elit euismod, accumsan volutpat urna cursus.'    
    },
    {
        'author':'rtg',
        'title':'blog 2',
        'date': '1-03-2022',
        'body':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse augue purus, viverra ornare erat at, suscipit vestibulum enim. Duis auctor ex vitae venenatis placerat. Ut egestas felis vitae velit tristique facilisis. Sed id augue placerat, sollicitudin tellus eu, interdum lacus. Cras rhoncus nulla ac fermentum blandit. Nulla a tincidunt dui. Morbi blandit ipsum ultricies elit euismod, accumsan volutpat urna cursus.'    
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == "__main__":
    app.run(debug=True)