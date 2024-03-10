Q1. Explain the relationship between the "Product" and "Product_Category" entities from the above    diagram.
Answer- The relationship that is observed between the “Product” table and the “Product_Category” table is a one-to-many relationship which means that for one product category can have many products but each product can belong only to one product category. 
Here we can also observe that the ‘id’ acts as a primary key to the “Product” table and foreign key to the “Product_Category” table and establishing the relationship between them. 

Q2. How could you ensure that each product in the "Product" table has a valid category assigned to it?
Answer- By using a Foreign key constraint on the “category_id” column we can ensure that each product in the “Product” table has a valid category. 
The Foreign key constraint enforces the referential integrity between the two tables. This way the database can check that each product has a valid category that exists in the “Product_Category” table.
