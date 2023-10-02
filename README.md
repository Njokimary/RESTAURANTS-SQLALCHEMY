Restaurant Review System
This project is a Python application built with SQLAlchemy for managing restaurant reviews. It allows you to create and manage restaurants, customers, and reviews, and provides various methods to query and interact with the data.

Installation
To get started, follow these steps:

Clone this repository to your local machine.
Install the required dependencies using Pipenv:

Object Relationship Methods
Review
Review.customer(): Returns the Customer instance for this review.
Review.restaurant(): Returns the Restaurant instance for this review.
Restaurant
Restaurant.reviews(): Returns a collection of all the reviews for the Restaurant.
Restaurant.customers(): Returns a collection of all the customers who reviewed the Restaurant.
Customer
Customer.reviews(): Returns a collection of all the reviews that the Customer has left.
Customer.restaurants(): Returns a collection of all the restaurants that the Customer has reviewed.
Aggregate and Relationship Methods
Customer
Customer.full_name(): Returns the full name of the customer, with the first name and last name concatenated Western style.
Customer.favorite_restaurant(): Returns the restaurant instance that has the highest star rating from this customer.
Customer.add_review(restaurant, rating): Creates a new review for the restaurant with the given restaurant_id.
Customer.delete_reviews(restaurant): Removes all their reviews for this restaurant.
Review
Review.full_review(): Returns a string formatted as follows:
Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
Restaurant
Restaurant.fanciest(): Returns one restaurant instance for the restaurant that has the highest price.
Restaurant.all_reviews(): Returns a list of strings with all the reviews for this restaurant formatted as follows:
"Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars."