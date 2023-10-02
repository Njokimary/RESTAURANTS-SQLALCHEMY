from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_url = "sqlite:///restaurants.db"
engine = create_engine(db_url)

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant', overlaps="customers")
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants', overlaps="reviews")
    
    def all_reviews(self):
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.rating} stars. - {review.comment}" for review in self.reviews]

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer', overlaps="restaurants")
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers', overlaps="reviews")
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        if self.reviews:
            return max(self.reviews, key=lambda review: review.rating).restaurant

    def add_review(self, restaurant, rating, comment):
        new_review = Review(restaurant=restaurant, customer=self, rating=rating,  comment=comment)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews', overlaps="customers,restaurants")
    customer = relationship('Customer', back_populates='reviews', overlaps="customers,restaurants")
    
    def full_review(self):
         return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars. - {self.comment}"
# Create the database schema
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a customer
customer1 = Customer(first_name="Njoki", last_name="Mary")
session.add(customer1)
session.commit()

customer2 = Customer(first_name="Brown", last_name="Ice")
session.add(customer2)
session.commit()
# Add a restaurant
restaurant1 = Restaurant(name="Pick $ GO", price=700)
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Tasty Pick", price=1000)
session.add(restaurant2)
session.commit()

# Add a review for the restaurant by the customer
customer1.add_review(restaurant2, rating=6, comment="A great dining experience.")

# Retrieve all reviews for the restaurant
restaurant_reviews = restaurant2.all_reviews()
for review in restaurant_reviews:
    print(review)
