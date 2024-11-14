# sturdy-memory
A simple inventory management system for the Mongoose system of SV Sticky. 

Fallacious rooster has been created as per request of the 18'th Commissioner of Internal Affairs, in order to keep track
of the "black box" the loss of products in the Mongoose sometimes can be.

## Development 
The guide below will tell you roughly how to get started with working on sturdy-memory.

## Koala
Sturdy-memory uses Koala for comparing successful transactions with the counted amount of the board member checking the
amount.

## Server setup
The server is written in.....? (To be determined)

### Endpoints
| Endpoint          | Method    | Function / Event                                                                                    | Data              |
|-------------------|-----------|:----------------------------------------------------------------------------------------------------|-------------------|
| `/add-product`    | POST      | When a product is added                                                                             | Product           |
| `/remove-product` | POST      | When a product is removed                                                                           | Product           |
| `/transaction`    | POST      | When a transaction has completed                                                                    | Items Bought      |
| `/product-status` | GET, POST | Get/set the quantity of a given product <br/>(For when a human counts the products in the basement) | Product, Quantity |

### Database Tables
| Table name    | Columns                                      |
|---------------|----------------------------------------------|
| current_stock | product_id <br/> product_name <br/> quantity |

## Frontend setup
The frontend is written in....? (To be determined)

# License
GNU GPL v3