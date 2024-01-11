**Please note: This website is made for educational purpose only.**

# Online Food Ordering System

Welcome to the Online Food Ordering System. This web application is designed to provide a seamless experience for users to browse and order delicious food items.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Preview](#preview)

## Features

- **Create New Food:**
  - Superusers can add new food items to the system.

- **View All Foods:**
  - Users can browse and view a list of all available food items.

- **Add to Cart:**
  - Users can add selected food items to their shopping cart.

- **View Cart:**
  - Users can view and manage items in their shopping cart.

- **User Authentication:**
  - Register: Users can create new accounts.
  - Login: Users can log in to their accounts.
  - Change Password: Users can change their account passwords.
  - Update User Information: Users can update their profile information.

## Technologies

This project uses the following technologies:

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Tailwind CSS:** A utility-first CSS framework that provides low-level utility classes to build designs directly in your markup.
- **HTML, CSS, and JavaScript:** Fundamental technologies for building web applications.

## Requirements

Make sure you have the following dependencies installed:

- Python
- Django
- NodeJs

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kimkorngmao/DjanFood.git
   cd DjanFood
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Install Tailwind CSS dependencies**
```
python manage.py tailwind install
```

6. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (for creating new food items):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up the superuser account.

## Usage

1. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

2. **Start Django Tailwind CSS:**

   ```bash
   python manage.py tailwind start
   ```

3. **Access the application in your web browser at `http://localhost:8000`.**

4. **Log in with the superuser credentials to create new food items.**

## Contributing

Feel free to contribute to the project. Please follow the [contribution guidelines](CONTRIBUTING.md).

# Preview
![image](https://github.com/kimkorngmao/DjanFood/assets/112237746/80188f54-a316-4e7a-9c42-a10542b18c44)

![image](https://github.com/kimkorngmao/DjanFood/assets/112237746/6e029e57-0559-4010-b91f-fe8d37b81b3a)

![image](https://github.com/kimkorngmao/DjanFood/assets/112237746/c6bfb273-28b0-4f12-aaed-ed9ab4ae7f11)

![image](https://github.com/kimkorngmao/DjanFood/assets/112237746/13236edb-d8e8-42db-b2f5-cd0a7c45827f)

![image](https://github.com/kimkorngmao/DjanFood/assets/112237746/3fbc7dbf-624c-4782-b32b-71f94f7049fc)

![image](https://github.com/kimkorngmao/DjanFood/assets/112237746/bf3e0a34-a4f5-44ce-9924-ee03d504b362)

![image](https://github.com/kimkorngmao/DjanFoodDeployment/assets/112237746/ce997301-4899-4fbe-a6e7-cb47406d4865)

![image](https://github.com/kimkorngmao/DjanFood/assets/112237746/a81149bf-6fcc-45d6-9896-71b4ddbf9487)

![image](https://github.com/kimkorngmao/DjanFood/assets/112237746/627aa9d0-7272-4f50-8a5b-268cd641979b)
