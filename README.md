# ATTEMPT BANK
This is a little Bank application done that allows users to attempt a few transactions from users who are likely to become our customers. It takes few personal details to register the user and send the information to a google worksheet that is connected through its API. It allows customers to deposit, withdraw or check balance and it updates the spreadsheet with customer details and information about each transaction made.


## Table of Contents

- [UX](#ux)
    - [User goals](#user-goals)
    - [User stories](#user-stories)
    - [Structure of the application](#structure-of-the-website)
- [Features](#features)
    - [Register](#register)
    - [Deposit](#deposit)
    - [Withdrawal](#withdrawal)
    - [Check Balance](#check-balance)
    - [Update Spreadsheet](#update-spreadsheet)

    
## UX

- ### User goals
- Application owner goals.
- We built this application to provide the users a mock Bank to attempt some transactions like an ATM Machine.
- It is done with the users in mind. It is well planned and programmed to give the user a wonderful experience for the fun of it.
 
- ### User stories
- To be able to practice the act of saving by depositing into ATTEMPT BANK.
- A User can also make withdrawals.
- They can also be able to view their balance.

- ### User stories as a customer
- I would like to register on the application to see how the transactions are made.
- What about giving ideas and sharing information with the programmer.

## Features

This application is a banking system that allows the users the ability to make deposit, withdrawal or check balance. And the transaction records are stored in a google spreadsheet with the help of its `Google Drive API` and `Google Sheets API`.
- ### Register
The application welcomes and requests the user to enter few details like their Names, Gender and Age. Then this information is stored to the connected google spreadsheet.
After registration the user receives an initial credit of $2000.
- ### Deposit
A user makes a deposit and the amount deposited is added to the initial deposit. The transaction is updated to the spreadsheet and displayed to the user. It allows up to 2000 as a maximum deposit.
- ### Withdrawal
The users can make withdrawals as well and it is deducted from the initial balance and the new account balance is is deisplayed to the user.
- ### Check Balance
This application provides the user the ability to check their balance as well. The balance is displayed to the user.

- ### Update Spreadsheet
The spreadsheet is used to store and retrieve the user details and transaction records.

### Deployment

`Github` and `Heroku` were used to deploy the application.
When you register for `Google Sheets API` and `Google Drive API`, you would get a JSON file with your credentials.

Register on Heroku, go to settings tab, create a _Config Var_ with KEY named `CREDS` and paste the content of your JSON file into the VALUE field.

Create another _Config Var_ with KEY named `PORT` and set the VALUE field to `8000`

Add two _Buildpacks_ and they must be in the order as follows:
1. `heroku/python`
2. `heroku/nodejs`

Next, go to the Deploy tab, select deployment method, and deploy.

[Back to Table of contents](#table-of-contents)

### Testing
The code was tested in CI Python Linter againt whitespaces



