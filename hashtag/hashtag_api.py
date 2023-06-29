from flask import Blueprint
hashtag_bp = Blueprint('hashtag',__name__,url_prefix='/hashtag')
from database.post_service import get_all_hashtag_db,get_exact_hasgtag_db
#get comment by count
@hashtag_bp.route('/',methods=['GET'])
def get_all_hashtags(size : int):
    get_hashtags = get_all_hashtag_db(size)

    if get_hashtags:
        return {'status':1,'message':get_hashtags}
    return {'status':0,'message':'Not found'}

# get define hashtag
@hashtag_bp.route('/<string:hashtag_name>',methods=['GET'])
def exact_hashtag(hashtag_name : str):
    hashtag = get_exact_hasgtag_db(hashtag_name)

    if hashtag:
        return {'status':1,'message':hashtag}
    return {'status':0,'mesage':"Not found"}
