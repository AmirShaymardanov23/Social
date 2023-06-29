from database.models import Post,PostPhoto,PostComment,db,Hashtag

# Получение всех постов
def get_all_posts_db():
    all_posts = Post.query.all()

    return all_posts


# Получение всех фото
def get_all_photos_db():
    all_photos = PostPhoto.query.all()

    return all_photos

# Получение всех фото юзера
def get_all_user_photo_db(user_id):
    exact_user_photo = PostPhoto.query.filter_by(user_id=user_id).all()

    return exact_user_photo

# Получение одного фото
def get_exact_photo_db(photo_id):
    exact_photo = PostPhoto.query.filter_by(photo_id=photo_id).first()

    return exact_photo

# Удалить фото
def delete_photo_db(photo_id,user_id):
    delete_photo = PostPhoto.query.filter_by(photo_id=photo_id,user_id=user_id).first()

    if delete_photo:
        db.session.delete(delete_photo)
        db.session.commit()
        return True
    return False
# изменение фотки
def change_photo_db(user_id,photo_id,photo_path):
    change_photo = PostPhoto.query.filter_by(user_id=user_id,photo_id=photo_id).first()

    if change_photo:
        change_photo.photo_path = photo_path
        db.session.commit()
        return True
    return False

# загрузка фотографии
def post_new_photo_db(user_id,photo_path):
    new_post_photo = PostPhoto(user_id = user_id , photo_path = photo_path )

    db.session.add(new_post_photo)
    db.session.commit()

    return new_post_photo.photo_id



# Создание нового поста
def add_new_post_db(user_id,photo_id,post_text):
    new_post = Post(user_id = user_id,photo_id = photo_id,post_text =post_text )

    db.session.add(new_post)
    db.session.commit()

    return new_post.post_id

# Получение поста
def get_exact_post_db(post_id):
    one_post = Post.query.filter_by(post_id=post_id).first()

    return one_post
# Удаление определенного поста
def delete_exact_post_db(post_id,user_id):
    delete_post = Post.query.filter_by(post_id=post_id,user_id=user_id).first()
    if delete_post:
        db.session.delete(delete_post)
        db.session.commit()
        return True
    return False

# Изменение описания под пост
def change_post_text_db(post_id,new_text):
    new_text = Post(post_id)

    db.session.add(new_text)
    db.session.commit()

# публикация поста
def publishing_post_db(user_id,post_text,hashtags):
    pass




# Добавление коммента ,  публикация
def add_comment_post_db(post_id,comment_user_id):
    add_post = PostComment.query.filter_by(post_id=post_id,comment_user_id=comment_user_id).first()

    db.session.add(add_post)
    db.session.commit()

# Получение конкретного коммента
def get_exact_comment_db(comment_id):
    exact_comment = PostComment.query.filter_by(comment_id=comment_id).first()

    return exact_comment

#изменение коммента
def change_comment_db(comment_id,comment_user_id):
    change_comment = PostComment.query.filter_by(comment_id,comment_user_id).first()

    db.session.add(change_comment)
    db.session.commit()

# Удаление коммента
def delete_comment_db(comment_id,user_id):
    delete_comment = PostComment.query.filter_by(comment_id=comment_id,user_id=user_id).first()

    if delete_comment:
        db.session.delete(delete_comment)
        db.session.commit()
        return True
    return False





# Получение хэштегов
def get_all_hashtag_db(size):
    get_hashtag = Hashtag.query.all()

    return get_hashtag[:size]

#Получение конкретного хэштега
def get_exact_hasgtag_db(hashtag_name):
    get_exact_hasgtag = Hashtag.filter_by(hashtag_name=hashtag_name).all()

    return get_exact_hasgtag

# добавить пост под хэштег
def create_post_for_hashtag(post_id,hastags):
    created_hashtags = []
    for hashtag_name in hastags:
        new_hashtag_post = Hashtag(post_id=post_id,hashtag_name=hashtag_name)
        created_hashtags.append(new_hashtag_post)

    db.session.add(created_hashtags)
    db.session.commit()

    return True








