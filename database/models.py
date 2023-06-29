from flask_sqlalchemy import SQLAlchemy

# создвем объект базы данных
db = SQLAlchemy()

# таблица пользователей
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String,nullable=False)
    birthday = db.Column(db.Date,nullable=False)
    register_date = db.Column(db.DateTime)


#таблица паролей
class Password(db.Model):
    __tablename__ = 'users passwords'
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'),primary_key=True)
    password = db.Column(db.String, nullable=False)


#таблица фото
class PostPhoto(db.Model):
    __tablename__ = 'user_photos'
    photo_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=False)
    photo_path = db.Column(db.String, nullable=False)

    user_fk = db.relationship(User)


#таблица постов
class Post(db.Model):
    __tablename__ = 'user_post'
    post_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    photo_id = db.Column(db.Integer,db.ForeignKey('user_photos.photo_id'),nullable=False)
    post_text = db.Column(db.Integer,nullable=True)
    post_date = db.Column(db.DateTime,nullable=False)


    user_fk = db.relationship(User)
    photo_fk = db.relationship(PostPhoto)

#таблица для комментов
class PostComment(db.Model):
    __tablename__ = 'post_comments'
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('user_post.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    comment_text = db.Column(db.Integer, nullable=True)
    post_date = db.Column(db.DateTime, nullable=False)


    user_fk = db.relationship(User)
    post_fk = db.relationship(Post)

# таблица хэштегов
class Hashtag(db.Model):
    __tablename__ = 'hashtags'
    hashtag_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('user_post.post_id'), nullable=False)
    hashtag_name = db.Column(db.String, nullable=False)

    post_fk = db.relationship(Post)
