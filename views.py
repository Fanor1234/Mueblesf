from flask import Blueprint, render_template

views = Blueprint(__name__,"views")



@views.route('/')
def Inicio():
    productos = [
        {'nombre':'mesa','precio':'200','fotos':'mesa.jpg',"id":0},
        {'nombre':'silla','precio':'300','fotos':'silla.jpg',"id":1},
        {'nombre':'estante','precio':'400','fotos':'estante.jpg',"id":2},
        {'nombre':'sillaplegable','precio':'600','fotos':'sillap.jpg',"id":3},
    ]
    return render_template('index.html', productos=productos)

@views.route('/about/')
def about():
    return render_template('about.html')

@views.route('/item/')
def item():
    return render_template('item.html')


@views.route('/producto/<int:post_id>')
def show_post(post_id):
    productos = [
        {'nombre':'mesa','precio':'200','fotos':'mesa.jpg'},
        {'nombre':'silla','precio':'300','fotos':'silla.jpg'},
        {'nombre':'estante','precio':'400','fotos':'estante.jpg'},
        {'nombre':'sillaplegable','precio':'600','fotos':'sillap.jpg'},
    ]
    item = productos[post_id]
    # show the post with the given id, the id is an integer
    return render_template('producto.html',item=item, post_id = post_id) 