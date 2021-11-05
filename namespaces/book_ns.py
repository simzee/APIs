# author_name : pawan bhosle
# updated on : 02 November 2021
from flask_restplus import Api, Resource, fields, reqparse, Namespace

nbook = Namespace('Books', description='Book-Api')
name_space2 = Namespace('Search book', description='school APIs')  # Pawan Bhosle

# book parser
bparser = reqparse.RequestParser()
bparser.add_argument('bid', type=int)
bparser.add_argument('bname', type=str)
bparser.add_argument('author', type=str)
bparser.add_argument('status', type=str)

bparser1 = reqparse.RequestParser()
bparser1.add_argument('bid', type=str)
bparser1.add_argument('bname', type=str)

bparser2 = reqparse.RequestParser()
bparser2.add_argument('bid', type=int)
bparser2.add_argument('bname', type=str)
bparser2.add_argument('status', type=str)

bparser3 = reqparse.RequestParser()
bparser3.add_argument('author', type=str)

# Pawan Bhosle
parser = reqparse.RequestParser()
parser.add_argument('member_name', type=str)
parser.add_argument('book_title', type=str)
parser.add_argument('status', type=str)

par = reqparse.RequestParser()
par.add_argument('bname', type=str)

pars = reqparse.RequestParser()
pars.add_argument('bid', type=int)

pa = reqparse.RequestParser()
pa.add_argument('bid', type=int)
pa.add_argument('status', type=str)

args = reqparse.RequestParser()
args.add_argument('member_id', type=int)

arge = reqparse.RequestParser()
arge.add_argument('member_id', type=int)
arge.add_argument('member_name', type=str)
