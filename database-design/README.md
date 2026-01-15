# 1 - Database Design

URL Used: https://www.pvcfittingsonline.com/collections/pvc-gate-valves/products/2-pvc-socket-gate-valve-spears-2022-020

## Prerequisites

- MySQL

## Instructions

1. Connect to your local MySQL server.

2. Create a schema named `product_details`.

3. Execute the following query:
```sql
-- Main product display
CREATE TABLE products (
	product_id INT PRIMARY KEY AUTO_INCREMENT,
    sku VARCHAR(8) NOT NULL UNIQUE,
    price DECIMAL(10, 2) NOT NULL,
    img_url VARCHAR(255) NOT NULL, -- Main image
    description TEXT NOT NULL
);

-- Description section (minus description)
CREATE TABLE product_description (
	attribute_id INT PRIMARY KEY AUTO_INCREMENT,
	product_id INT NOT NULL,
    attribute_name VARCHAR(100) NOT NULL, -- Example: Material
    attribute_value VARCHAR(255) NOT NULL, -- Example: PVC
	FOREIGN KEY (product_id) 
		REFERENCES products(product_id)
        ON DELETE CASCADE
);

-- Additional info section
CREATE TABLE product_additional_info (
	info_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    info_name VARCHAR(100) NOT NULL, -- Example: Size in Inches
    info_value VARCHAR(255) NOT NULL, -- Example: 3/4 inch
	FOREIGN KEY (product_id) 
		REFERENCES products(product_id)
        ON DELETE CASCADE
);
```
