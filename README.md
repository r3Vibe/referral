# Referral System Assignment

---

## Description

Basic referral system done with FastApi. Includes 4 Endpoints

- Register User
- Login User
- User Details
- List Referred Signups

For easy installation i have used pipenv.

---

## Installation

- Clone the project form github
  `git clone https://github.com/r3Vibe/referral.git`

---

## Usage

- Update .env
  ```
      DB_URL= mongodb://mongodb:27017 (For Docker Only)
      DB_NAME= database name
      SECRET=  jwt secret
  ```
- Run via Docker
  `docker-compose up`

- Access Url
  `http://127.0.0.1:8000/docs`

---