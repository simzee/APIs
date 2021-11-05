# author_name : pawan bhosle
# updated on : 02 November 2021
from flask_restplus import Api, Resource, fields, reqparse, Namespace


nstudent = Namespace('Member/Admin', description="Member-Api")
name_space = Namespace('Member/Student-Staff', description='Member-Api')

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

# student parsers
sparser = reqparse.RequestParser()
sparser.add_argument('member_id', type=int)
sparser.add_argument('member_name', type=str)
sparser.add_argument('book_title', type=str)

sparser1 = reqparse.RequestParser()
sparser1.add_argument('member_id', type=int)
sparser1.add_argument('member_name', type=str)

sparser3 = reqparse.RequestParser()
sparser3.add_argument('designation', type=str)
