from flask import Flask
from app.controller import get_user, save_user, update_user, delete_user

# geekforgeek
# kumarrvipin99@gmail.com
# Vipin@*8990



# courera
# 0201csai077@niet.co.in
# Maurya@123

app = Flask(__name__)



@app.route('/')
def hello():
    return "It's working fine"

@app.route('/get-user', methods=['GET'])
def user_1():
    return get_user(), 200

@app.route('/save-user', methods=['POST'])
def user_2():
    return save_user()

@app.route('/update-user', methods=['PUT'])
def user_3():
    return update_user()

@app.route('/delete-user', methods=['DELETE'])
def user_4():
    return delete_user()

if __name__ == '__main__':
    app.run(debug = True)