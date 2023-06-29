from flask import Blueprint,request
from database.post_service import get_exact_comment_db,delete_comment_db,add_comment_post_db,change_comment_db
comment_bp = Blueprint('comment',__name__,url_prefix='/comment')

# get user's post
@comment_bp.route('/<int:post_id>',methods=['GET'])
def get_exact_comment(post_id : int):
    exact_comment = get_exact_comment_db(post_id)

    if exact_comment:
        return {'status':1,'message':exact_comment}
    return {'status': 0, 'message': 'Not found'}

# publishing comment
@comment_bp.route('/<int:post_id>/<int:comment_user_id>',methods=['POST'])
def publish_comment(post_id : int,comment_user_id):
    publish_comment = request.json.get('comment_text')
    add_comment_post_db(post_id,comment_user_id)
    return {'message': publish_comment}
# change comment
@comment_bp.route('/<int:comment_id>/<int_comment_user_id>',methods=['PUT'])
def change_comment(comment_id : int , comment_user_id : int):
    new_text = request.json.get('new_text')
    change_comment_db(comment_id,comment_user_id)
    return {'message':new_text}

# delete comment
@comment_bp.route('/<int_comment_id>/<int:comment_user_id>',methods=["DELETE"])
def delete_comment(comment_id : int,comemnt_user_id : int):
    delete_comment = delete_comment_db(comment_id,comemnt_user_id)

    if delete_comment:
        return {'status': 1, 'message': delete_comment}
    return {'status': 0, 'message': 'Not found'}