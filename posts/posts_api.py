from flask import Blueprint,request
from database.post_service import get_all_posts_db,get_exact_post_db,delete_exact_post_db,change_post_text_db, add_new_post_db,post_new_photo_db,create_post_for_hashtag
post_bp = Blueprint('user_post',__name__,url_prefix='/post')

# get all posts
@post_bp.route('/',methods=['GET'])
def get_all_user_posts():
    all_posts = get_all_posts_db()

    if all_posts:
        return {'status':1,'message':all_posts}
    return {'status':0, 'message':'Not found'}

#get define post
@post_bp.route('/<int:post_id>',methods=['GET'])
def get_exact_post(post_id : int):
    exact_post = get_exact_post_db(post_id)

    if exact_post:
        return {'status':1,'message':exact_post}
    return {'status':0,'message':'Not found'}

#change user's post
@post_bp.route('/<int:post_id>',methods=['PUT'])
def change_user_post(post_id : int):
    new_post_text = request.json.get('new_post_text')

    change_post_text_db(post_id,new_post_text)

    return {'status': 1, 'message': 'Changed'}

#delete user's post
@post_bp.route('/<int:user_id>/<int:post_id>',methods=['DELETE'])
def delete_user_post(user_id : int, post_id : int):
    delete_post = delete_exact_post_db(post_id, user_id)

    if delete_post:
        return {'status':1,'message':'post deleted'}
    return {'status':0 , 'message':'Not Found'}


#publish post
@post_bp.route('/upload_post',methods=['POST'])
def create_post(post_text : str,user_id : int):
    # получение из фронт части фото
    file = request.files.get('post_photo','')
    file.save(f'user_images/{file.filename}')

    #получение хэштегов из фронта
    hashtags = request.json.get('hashtags')


    # сохранение фото id в базу
    new_photo_id = post_new_photo_db(user_id, file.filename)

    # сохрвнение поста
    new_post = add_new_post_db(user_id = user_id , photo_id=new_photo_id,post_text=post_text)
    if hashtags:
        create_post_for_hashtag(new_post,hashtags)

    return {'status':1,'message':'Post created'}
