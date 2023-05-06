from flask import Flask, request, jsonify, render_template
import os,re, datetime
from models import Book
import db

app = Flask(__name__)

if not os.path.isfile('books.db'):
    db.connect()


@app.route("/")
def index():
    return render_template('index.html')

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return True
    else:
      return False
    
@app.route("/request", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    email = req_data['email']
    if not isValid(email):
      return jsonify({
         'status': '422',
         'res': 'failure',
         'error': 'Invalid email'})
    title = req_data['title']
    bks = [b.serialize() for b in db.view()]
    for b in bks:
      if b['title'] == title:
         return jsonify({
            'status': '404',
            'res': 'failure',
            'error': 'Book already exists'})
      
    bk = Book(db.getNewId(), True, title, datetime.datetime.now())
    print('new book', bk.serialize())
    db.insert(bk)

    new_bks = [b.serialize() for b in db.view()]
    print('new book in lin:', new_bks)
    return jsonify({
       'res': bk.serialize(),
         'status': '200',
         'message': 'Book added successfully'})

@app.route("/request", methods=['GET'])
def getRequest():
   content_type = request.headers.get('Content-Type')
   bks =[b.serialize() for b in db.view()]
   if(content_type == 'application/json'):
      json = request.json
      for b in bks:
         if b['id'] == int(json['id']):
            return jsonify({
               'res': b,
               'status': '200',
               'message': 'Book found successfully'})
         return jsonify({
                'status': '404',
                'res': 'failure',
                'error': 'Book not found'})
   else:
      return jsonify({
            'res': bks,
            'status': '200',
            'msg': 'Books found successfully',
            'no_of_books': len(bks)})
   
@app.route("/request/<id>", methods=['GET'])
def getRequestById(id):
   req_args = request.view_args
   bks =[b.serialize() for b in db.view()]
   if req_args:
    for b in bks:
        if b['id'] == int(req_args['id']):
            return jsonify({
                'res': b,
                'status': '200',
                'message': 'Book found successfully'})
    return jsonify({
            'status': '404',
            'res': 'failure',
            'error': 'Book not found'})
   
@app.route("/request/", methods=['PUT'])
def putRequest():
   req_data = request.get_json()
   available = req_data['available']
   title = req_data['title']
   id = req_data['id']
   bks =[b.serialize() for b in db.view()]
   for b in bks:
      if b['id'] == id:
            bk = Book(id, available, title, datetime.datetime.now())
            db.update(bk)
            return jsonify({
                    'res': bk.serialize(),
                    'status': '200',
                    'message': 'Book updated successfully'})
   return jsonify({
            'status': '404',
            'res': 'failure',
            'error': 'Book not found'})

@app.route("/request/<id>", methods=['DELETE'])
def deleteRequest(id):
   req_args = request.view_args
   bks =[b.serialize() for b in db.view()]
   if req_args:
    for b in bks:
        if b['id'] == int(req_args['id']):
            db.delete(int(req_args['id']))
            return jsonify({
                'res': b,
                'status': '200',
                'message': 'Book deleted successfully'})
    return jsonify({
            'status': '404',
            'res': 'failure',
            'error': 'Book not found'})