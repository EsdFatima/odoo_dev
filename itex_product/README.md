# Products Odoo Module

## Overview
This Odoo module provides a simple yet effective solution for managing products. It includes a "Product" model with essential fields and features. Follow the instructions below to understand the module's structure and functionality.
## Features
1. **Product Model:**
    - Fields:
        - `name`: Name of the product.
        - `description`: Description of the product.
        - `unit_price`: Unit price of the product.
        - `quantity`: Quantity of the product.
        - `total_price`: Computed field that calculates the total price based on quantity and unit price.
    
      
2. **Computed Field:**
    - The module utilizes a computed field (`total_price`) to automatically calculate the total price whenever changes are made to the `quantity` or `unit_price` fields.
   

## Installation
1. Clone or download this module from the provided repository.
2. Install the module via the Odoo App interface.
3. Start create your products records efficiently.

## Usage
-Product Management:

    - Navigate to the "Poduct Module" in the Odoo interface to manage products.
    - Add or edit products, providing details such as name, description, price, quantity.







