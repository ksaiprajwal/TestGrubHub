from flask import Blueprint, request, Response, jsonify
from flask_login import login_required
from app.models import User, Business, Tags, Reviews
## TODO CHECK PATHING ABOVE
from flask_login import current_user

business_routes = Blueprint("businesses", __name__)

## BUSINESS ROUTE FOR GET BUSSINESS OWNED BY CURRENT USER
@business_routes.route("/current", methods=["GET"])
@login_required
def get_businesses_of_curr_user():
  businesses = Business.query.filter(Business.owner_id == current_user.id).all()
  return {"businesses":[business.to_dict() for business in businesses]}

## GET BUSINESS BY ID
@business_routes.route("/<int:id>")
def get_business_by_id(id):
  business = Business.query.get(id)

  if not business:
    return {"message":"Business couldn't be found", "statusCode": 404}
  pass ## TODO FINISH THIS
