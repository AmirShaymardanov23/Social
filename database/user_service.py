from database.models import User,Password,db

# Регистрация
def register_user_db(**user_data):
    new_user = User(**user_data)

    db.session.add(new_user)
    db.session.commit()

#Проверка по email
def check_user_db(email):
    email = User.query.filter_by(email=email).first()

    if email:
        return True
    return False


# Проверка пароля
def check_user_password_db(email,password):
   checker = Password.query.filter_by(email=email,password=password).first()

   if checker:
       return True
   return False


#  Получение юзеров
def get_all_users_db():
    all_users = User.query.all()

    return all_users


# Получение одного юзера
def get_exact_user_db(user_id):  #filter_by().first
    exact_user = User.query.filter_by(user_id=user_id).first()

    return exact_user


# Удаление юзера
def delete_user_db(user_id):
    delete_user = User.query.filter_by(user_id=user_id).first
    if delete_user:
        db.session.delete(delete_user)
        db.session.commit()
        return True
    return False