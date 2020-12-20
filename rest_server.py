from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

shares=[
    {"id":1, "Symbol": "APPL", "Name": "Apple inc.", "Price":117},
    {"id":2, "Symbol": "PFE", "Name": "Pfizer", "Price":37},
    {"id":3, "Symbol": "WFC", "Name": "Wells & Fargo", "Price":29 }
]
nextId=4

@app.route('/')
def index():
    return "hello"
# get all
@app.route('/shares')
def getAll():
    return jsonify(shares)
# find by id
@app.route('/shares/<int:id>')
def findByID(id):
    foundShares = list(filter (lambda t: t["id"]== id, shares))
    if len(foundShares) == 0:
        return jsonify({}), 204
    return jsonify(foundShares[0])
    return "served by find id with it " + str(id)

# create
#  curl -X POST -H "content-type:application/json" -d "{\"Symbol\":\"test\", \Name\":\"some guy\", \"Price\": 123}" http://127.0.0.1:5000/shares
@app.route('/shares', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)

    share = {
        "id": nextId,
        "Symbol": request.json["Symbol"],
        "Name": request.json["Name"],
        "Price": request.json["Price"]
    }
    shares.append(share)
    nextId += 1
    return jsonify(share)

    return "served by Create() " 
# update
# curl -X PUT -d "{\"Symbol\":\"new Symbol\", \"Price\": 999}" -H "content-type:application/json"  http://127.0.0.1:5000/shares/1
@app.route('/shares/<int:id>', methods=['PUT'])
def update(id):
    foundShares = list(filter (lambda t: t["id"]== id, shares))
    if len(foundShares) == 0:
        return jsonify({}), 404
    currentShare = foundShares[0]
    if 'Title' in request.json:
        currentShare['Title'] = request.json['Title']
    if 'Name' in request.json:
        currentShare['Name'] = request.json['Name']
    if 'Price' in request.json:
        currentShare['Price'] = request.json['Price']

    return jsonify(currentShare)

# delete
# curl -X DELETE http://127.0.0.1:5000/shares/1
@app.route('/shares/<int:id>', methods=['DELETE'])
def delete(id):
    foundShares = list(filter (lambda t: t["id"]== id, shares))
    if len(foundShares) == 0:
        return jsonify({}), 404
        shares.remove(foundShares[0])
    return jsonify({"done":True})

    # ********Also have to do client side - client side from Lab - client side interacting with server********


if __name__=="__main__":
    print("in if")
    app.run(debug=True)