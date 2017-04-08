from flask_sqlalchemy import SQLAlchemy
from flask_app import app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yagami:deathnote@localhost/e_flask'


db=SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Database models

class Customer(db.Model):

	__tablename__ = "customer"

	id=db.Column('customer_id',db.String(20),primary_key=True)
	first_name=db.Column('first_name',db.String(20))
	last_name=db.Column('last_name',db.String(20))
	loginid=db.Column('loginid',db.String(10),unique=True)
	passwd=db.Column('passwd',db.String(20),unique=True)
	contact_num=db.Column('contact_num',db.String)

class order(db.Model):

	__tablename__ = "aboutorder"		
	
	id=db.Column('order_id',db.String(20),primary_key=True)
	order_num=db.Column('order_num',db.Integer)
	ship_via=db.Column('ship_via',db.String(20))
	shipper_ID=db.Column('shipper_ID',db.String(20))
	order_date=db.Column('order_date',db.Date)
	shipped_date=db.Column('shipped_date',db.Date)

	customer_ID=db.Column('customer',db.String(20),db.ForeignKey('customer.customer_id'))

class BillingInfo(db.Model):

	__tablename__ = "billinginfo"

	id=db.Column('billing_id',db.String(40),primary_key=True)
	credit_card_pin=db.Column('credit_card_pin',db.Integer)
	credit_card_num=db.Column('credit_card_num',db.Integer)
	bill_date=db.Column('bill_date',db.Date)
	billing_addr=db.Column('billing_addr',db.String)
	credit_card_expiry=db.Column("credit_card_expiry",db.Date)
	
	cust_ID=db.Column('customer',db.String(20),db.ForeignKey('customer.customer_id'))
	order_ID=db.Column('aboutorder',db.String(20),db.ForeignKey('aboutorder.order_id'))


class Shipper(db.Model):

	__tablename__ = "shipper"

	id=db.Column('shipper_id',db.String(40),primary_key=True)
	phone=db.Column(db.String(20))
	company_name=db.Column(db.String(20))

	order_ID=db.Column('aboutorder',db.String(20),db.ForeignKey('aboutorder.order_id'))

class Category(db.Model):

	__tablename__ = "category"

	id=db.Column('category_id',db.String(20),primary_key=True)
	category_name=db.Column('category_name',db.String(20))
	description=db.Column('description',db.String(50))

class Product(db.Model):

	__tablename__ = "product"

	id=db.Column('product_id',db.String(20),primary_key=True)
	quantity_pu=db.Column('quantity_pu',db.Integer)
	product_name=db.Column('product_name',db.String(20))
	stock_units=db.Column('stock_units',db.Integer)
	unit_weight=db.Column('unit_weight',db.Float)
	discount=db.column('unit_weight',db.Float)
	reorder_level=db.Column('discount',db.Integer)
	product_description=db.Column(db.String(30))
	supplier_ID=db.Column(db.String(20))

	category_ID=db.Column('category',db.String(20),db.ForeignKey('category.category_id'))		

class Cart(db.Model):

	__tablename__ = "cart"

	id=db.Column('cart_id',db.String(20),primary_key=True)
	nop=db.Column('nop',db.Integer)
	total_price=db.Column('total_price',db.Integer)

	customer_ID=db.Column('customer',db.String(20),db.ForeignKey('customer.customer_id'))


class OrderDetails(db.Model):

	__tablename__ = "orderdetails"

	id=db.Column('useless_id',db.Integer,primary_key=True)
	unit_price=db.column('unit_price',db.Float)
	discount=db.column('discount',db.Float)
	order_num=db.Column('order_num',db.Integer)
	quantity=db.Column('quantity',db.Integer)

	product_ID=db.Column('product',db.String(20),db.ForeignKey('product.product_id'))
	order_ID=db.Column('aboutorder',db.String(20),db.ForeignKey('aboutorder.order_id'))


class TrackingInfo(db.Model):

	__tablename__ = "trackinginfo"

	id=db.Column('tracking_id',db.String(20),primary_key=True)
	delivery_date=db.Column('delivery_date',db.Date)
	shipped_date=db.Column('shipped_date',db.Date)

	product_ID=db.Column('product',db.String(20),db.ForeignKey('product.product_id'))
	order_ID=db.Column('aboutorder',db.String(20),db.ForeignKey('aboutorder.order_id'))


class Supplier(db.Model):

	__tablename__ = "supplier"

	id=db.Column('supplier_id',db.String(20),primary_key=True)
	first_name=db.Column('first_name',db.String(20),primary_key=True)
	last_name=db.Column('last_name',db.String(20),primary_key=True)	


class PersonalInfo(db.Model):

	__tablename__ = "personal_info"

	id=db.Column('dummy_id',db.String(20),primary_key=True)
	phone=db.Column('first_name',db.String(20))
	address=db.Column('address',db.String(80))
	city=db.Column('city',db.String(10))
	country=db.Column('country',db.String(20))
	postal_code=db.Column('postal_code',db.Integer)
	email=db.Column(db.String(30), unique=True)
	passwd=db.Column('passwd',db.String(20))
	login_id=db.Column('login_id',db.String(20),unique=True)

	customer_ID=db.Column('customer',db.String(20),db.ForeignKey('customer.customer_id'))


class Admin(db.Model):

	__tablename__ = "admin"

	id=db.Column('admin_id',db.String(20),primary_key=True)
	first_name=db.Column('first_name',db.String(20))
	last_name=db.Column('last_name',db.String(20))
	login_ID=db.Column('login_ID',db.String(20))
	admin_pwd=db.Column('admin_pwd',db.String(20))


if __name__ == '__main__':
    manager.run()

