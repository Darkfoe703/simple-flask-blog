import os, markdown, frontmatter
from datetime import datetime
from flask import Blueprint, render_template, url_for

blog = Blueprint('blog', __name__)

POSTS_FOLDER = os.path.join(os.path.dirname(__file__), 'posts')

def get_posts():
    """Lee los archivos Markdown y devuelve una lista de posts con sus metadatos."""
    posts = []
    for filename in os.listdir(POSTS_FOLDER):
        if filename.endswith('.md') or filename.endswith('.markdown'):
            filepath = os.path.join(POSTS_FOLDER, filename)
            with open(filepath, 'r') as file:
                post = frontmatter.load(file)# Procesar metadatos
                posts.append(
                    {
                        "title": post.get("title", "Untitled"),
                        "author": post.get("author", "Anonymous"),
                        "date": datetime.strptime(
                            post.get("date", ""), "%Y-%m-%d %H:%M:%S %z"
                        ).strftime("%d %b, %Y"),
                        "slug": post.get("slug", filename.replace(".md", "")),
                        "excerpt": post.get("excerpt", ""),
                        "image": post.get("image", ""),
                        "content": markdown.markdown(
                            post.content
                        ),  # Convertir el contenido Markdown a HTML
                    }
                )
    # Ordenar posts por fecha (más recientes primero)
    posts.sort(key=lambda x: x['date'], reverse=False)
    return posts

@blog.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@blog.route('/no-sidebar')
def no_sidebar():
    return render_template('no-sidebar.html')

@blog.route('/single-post')
def single_post():
    return render_template('single-post.html')

@blog.route('/post/<slug>')
def post_detail(slug):
    """Renderiza el detalle de un post usando su slug."""
    for filename in os.listdir(POSTS_FOLDER):
        if filename.endswith('.md'):
            filepath = os.path.join(POSTS_FOLDER, filename)
            with open(filepath, 'r') as file:
                post = frontmatter.load(file)
                if post.get('slug') == slug:
                    content = markdown.markdown(post.content)
                    return render_template(
                        "post_detail.html",
                        title=post.get("title", "Sin título"),
                        author=post.get("author", "Anónimo"),
                        date=datetime.strptime(
                            post.get("date", ""), "%Y-%m-%d %H:%M:%S %z"
                        ).strftime("%d %b, %Y"),
                        excerpt=post.get("excerpt", ""),
                        image=post.get("image", ""),
                        content=content,
                    )
    return "Post no encontrado", 404
