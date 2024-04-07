# Referral System Assignment

---

## Description

Basic referral system done with FastApi. Includes 4 Endpoints

- Register User
- Login User
- User Details
- List Referred Signups

For easy installation i have used pipenv.

## Important

The boilerplate used in this project is completly mine. You will need to have a
mongodb atlas account or local mongodb server running to use this. Beanie ODM was
used for database communications.

---

## Installation

- Clone the project form github
  `git clone https://github.com/r3Vibe/referral.git`

- Install Dependencies
  `pipenv install`

---

## Usage

- Update .env
  ```
      DB_URL= local database url or atlas url
      DB_NAME= database name
      SECRET=  jwt secret
  ```
- Run server
  `uvicorn app.main:app --reload`

- Access Url
  `http://127.0.0.1:8000/docs`
