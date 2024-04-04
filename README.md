# KeDA Material Registration Odoo Module

## Overview
The Keda Material Registration module is an Odoo addon designed to manage material registration within the Keda system. This module allows users to register materials, update their details, and delete them as necessary.

## Features
- Register new materials with details such as name, code, type, price, and related supplier.
- Update existing material details, including buy price.
- Delete materials from the system.

## Installation
1. Clone or download this repository to your Odoo addons directory.
2. Restart your Odoo instance.
3. Install the "Keda Material Registration" module from the Odoo Apps interface.
4. Configure the module settings as needed.

## Usage
- After installation, navigate to the "Materials" menu in the Odoo interface to access the material registration functionalities.
- Materials can also be managed programmatically using the provided API endpoints.

## API Endpoints

### 1. `registered-material` Endpoint
- **Method**: GET
- **URL**: `/registered-material`
- **Description**: Retrieves a list of registered materials.
- **Request Body**: N/A
- **Response Body**: Array of material objects, each containing the following attributes:
  - `id`: Material ID (Integer)
  - `name`: Material name (String)
  - `mat_code`: Material code (String)
  - `mat_type`: Material type (String)
  - `buy_price`: Material buy price (Float)
  - `partner_name`: Related supplier name (String)

### 2. `update-material` Endpoint
- **Method**: PATCH
- **URL**: `/update-material/<int:material_id>`
- **Description**: Updates the buy price of a material with the specified ID.
- **Request Body**: JSON object with the following attributes:
  - `buy_price`: New buy price for the material (Float)
- **Response Body**: Success message if the update is successful.

### 3. `delete-material` Endpoint
- **Method**: DELETE
- **URL**: `/delete-material/<int:material_id>`
- **Description**: Deletes the material with the specified ID from the system.
- **Request Body**: JSON object with the following attribute:
  - `delete`: Set to `true` to confirm deletion (Boolean)
- **Response Body**: Success message if the deletion is successful.

## Unit Testing
- Unit tests for the module can be found in the `tests` directory.
- To run the unit tests using Odoo's testing framework, execute the following command in your terminal:
  ```bash
  ./odoo-bin -d your_database_name --test-enable -u your_module_name
