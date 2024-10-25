Here’s the README formatted so you can directly paste it into your README file:

---

# MakersBnB

A back-end and front-end accommodation booking application inspired by Airbnb, developed collaboratively in an agile environment with sprints and test-driven development (TDD) practices.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Project Overview
MakersBnB is a full-stack accommodation booking site that allows users to browse listings, create new listings, and make bookings. This project was created by an agile team with a focus on following TDD principles to ensure a reliable, scalable, and user-friendly platform. It includes user authentication, interactive listings, and booking confirmations.

## Features
- **User Authentication**: Allows users to register and log in.
- **Browse Listings**: Users can view available accommodation listings.
- **Create Listings**: Users can create and manage their own listings.
- **Booking Confirmations**: Users can make and confirm bookings.

## Tech Stack
- **Back-End**: Python, Flask
- **Front-End**: HTML, CSS
- **Database**: PostgreSQL
- **Testing**: TDD with Pytest and other relevant testing tools

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/MakersBnB.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd MakersBnB
   ```
3. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up the database**:
   - Create a PostgreSQL database and update the database URI in the configuration file.
   - Run migrations to set up tables.

6. **Run the application**:
   ```bash
   flask run
   ```
7. **Access the app**: Open your browser and go to `http://127.0.0.1:5000`.

## Usage
1. **Register/Login**: Users can create an account or log in to access listings.
2. **View Listings**: Browse through available accommodation options.
3. **Create Listings**: Registered users can add new listings with details.
4. **Book Accommodations**: Users can select listings and confirm their bookings.

## Project Structure
- **app/**: Contains the main application files and modules.
- **templates/**: HTML templates for the app’s front-end.
- **static/**: CSS files for styling.
- **tests/**: Test cases for various components of the application.

