from flask import *
from app.user import bp
from app.extensions import db
from app.models.user import User
from app.utils.common_utils import *

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        user = User(id=generateId(), name=name, email=email)
        db.session.add(user)
        db.session.commit()
        flash("User has been added", "success")
        return redirect(url_for('user.index'))
    
    return render_template('create.html')

@bp.route('/delete/<user_id>')
def delete(user_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    flash("User has been deleted", "success")
    return redirect(url_for('user.index'))

@bp.route('/edit/<user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    if request.method == "POST":
        if user:
            user.name = request.form["name"]
            user.email = request.form["email"]
            db.session.commit()
            flash("User has been updated", "success")
        else:
            flash("Can't Update User", "error")
        return redirect(url_for('user.index'))
    
    return render_template('edit.html', user=user)