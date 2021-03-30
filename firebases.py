import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyACjvHy9WX_Cx0NC8B24I1UIiGBC8ifyNA",
    "authDomain": "smart-farm-3ef1a.firebaseapp.com",
    "databaseURL": "https://smart-farm-3ef1a.firebaseio.com",
    "projectId": "smart-farm-3ef1a",
    "storageBucket": "smart-farm-3ef1a.appspot.com",
    "messagingSenderId": "849173162919",
    "appId": "1:849173162919:web:542600f2780ef5ed93e482",
    "measurementId": "G-XQ2P0TX564",
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# push data auto key
# data = {"status_led":1}
# db.push(data)

# push data define key
# data = {"status_led": 0}
# db.child("my_led").set(data)

# update data
# data = {"status_led": 0}
# db.child("my_led").update(data)


def stream_handler(message):
    # print(message["event"])  # put
    #print(message["path"])  # /-K7yGTTEp7O549EzTYtI
    #print("the current status LED = {}".format(message["data"]["status_led"]))
    print(message["data"])  # {'title': 'Pyrebase', "body": "etc..."}

    # return message["data"]


# my_stream = db.child("my_led").stream(stream_handler)
my_stream = db.child("my_led").stream(stream_handler)
print(my_stream)

# data = "hi haha"
# print("status led is {}".format(data)
