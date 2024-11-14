# Setup

## Server
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

## Front-end
The frontend is written in....? (To be determined)