from sanic import Sanic,response
from sanic.log import logger
from sanic.response import text,json
import logging
import names

#This is for TESTING PURPOSES ONLY YOU SHOULD ALWAYS LOAD THE CONFIG VARS FOR ENV VARS AND USE A PERSISTENT DB
#app = Sanic(__name__, load_env='CMPAPI_')
app = Sanic(__name__)

#Logging all the INFO localy only for this test, this should be handled properly, for the access logs it should be get from the ALB and saved to S3, and then analize-it with Athena. 
logging.basicConfig(filename='logs.log',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Inmemory DB, is not the best practice, but is the quickest way to do it and allowed on the test, the best way obviously is with a HA Persistent DB.
user_db = {}
user_id = 0

@app.route("/")
async def start(request):
    return text('Hello!! This is Ivan Mina CMP API',status=200)

@app.route('/user/<user_id_request>', methods=['GET'])
async def get_handler(request,user_id_request):
    global user_db
    return text('GET - {}'.format(user_db.get(int(user_id_request))),status=200)

@app.route('/user', methods=['POST'])
async def post_handler(request):
    global user_id
    global user_db
    user_id += 1
    username = names.get_first_name()
    user_db[user_id] = username
    return text('POST - User {} has been added to the DB'.format(username),status=201)

@app.route('/user/<user_id_request>', methods=['DELETE'])
async def delete_handler(request,user_id_request):
    global user_db
    user = user_db.get(int(user_id_request))
    try:
        user_db.pop(int(user_id_request))
        return text('DELETE - The User {} has been deleted'.format(user),status=200)
    except KeyError:
        return text("DELETE - The User with ID {} doesn't exist".format(user_id_request),status=404)

@app.route('/allusers', methods=['GET'])
async def allusers_handler(request):
    global user_db
    return text('DB DUMP - {}'.format(user_db.items()),status=200)

@app.route('/health', methods=['GET'])
def handle_request(request):
    return text("Healthy!",status=200)

if __name__ == "__main__":
    # Because we dont use and ALB and we want to saw the access log, for now we leave it enabled.
    app.run(host="0.0.0.0", port=80, debug=False, access_log=True)
