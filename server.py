from flask import Flask, url_for, request, redirect, abort, jsonify
from SharesDao import shareDao
#from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='staticpages')
#CORS(app)

@app.route('/')
def index():
    return "hello"
#get all


@app.route('/shares')
def getAll():
    return jsonify(shareDao.getAll())
# find By id


@app.route('/shares/<int:id>')
def findById(id):
    return jsonify(shareDao.findById(id))

# create
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/shares


@app.route('/shares', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    share = {
        "id": request.json["id"],
        "symbol": request.json["symbol"],
        "name": request.json["name"],
        "price": request.json["price"]
    }
    return jsonify(shareDao.create(share))

    return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/shares/1


@app.route('/shares/<int:id>', methods=['PUT'])
def update(id):
    foundShare=shareDao.findById(id)
    print (foundShare)
    if foundShare == {}:
        return jsonify({}), 404
    currentShare = foundShare
    if 'symbol' in request.json:
        currentShare['symbol'] = request.json['symbol']
    if 'name' in request.json:
        currentShare['name'] = request.json['name']
    if 'price' in request.json:
        currentShare['price'] = request.json['price']
    shareDao.update(currentShare)

    return jsonify(currentShare)

#delete
# curl -X DELETE http://127.0.0.1:5000/shares/1


@app.route('/shares/<int:id>', methods=['DELETE'])
def delete(id):
    shareDao.delete(id)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)