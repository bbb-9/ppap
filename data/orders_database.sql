CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

-- Insert sample data into the orders table
INSERT INTO orders (order_id, customer_id, order_date, total_amount)
VALUES
    (1, 101, '2023-08-01', 150.00),
    (2, 102, '2023-08-02', 230.45),
    (3, 103, '2023-08-03', 50.20),
    (4, 101, '2023-08-03', 120.80),
    (5, 104, '2023-08-04', 75.60);

    CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

-- Insert sample data into the customers table
INSERT INTO customers (customer_id, first_name, last_name, email)
VALUES
    (101, 'John', 'Doe', 'john@example.com'),
    (102, 'Jane', 'Smith', 'jane@example.com'),
    (103, 'Michael', 'Johnson', 'michael@example.com'),
    (104, 'Emily', 'Williams', 'emily@example.com');

-- Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Insert sample data into the products table
INSERT INTO products (product_id, product_name, price)
VALUES
    (1, 'T-shirt', 20.00),
    (2, 'Jeans', 45.50),
    (3, 'Shoes', 60.00),
    (4, 'Hat', 15.25);

-- Linking table for orders and products (many-to-many relationship)
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT
);

-- Insert sample data into the order_items table
INSERT INTO order_items (order_item_id, order_id, product_id, quantity)
VALUES
    (1, 1, 1, 2),
    (2, 1, 3, 1),
    (3, 2, 2, 1),
    (4, 3, 1, 3),
    (5, 3, 4, 2);

