from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
        <head><title>🚀 DevOps Journey</title></head>
        <body style="text-align: center; font-family: Arial; margin-top: 100px;">
            <h1>🚀 Hello, I'm Khobaib!</h1>
            <h2 style="color: #2E86C1;">I'm mastering CI/CD with GitHub Actions & AWS ECS 💻☁️</h2>
            <p>Stay tuned for more exciting DevOps adventures! 🔧📦🌐</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
