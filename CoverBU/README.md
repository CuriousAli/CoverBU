# Name - Cover Build-Up


## Description:

### Create backend part of app for work with Cover Build-Up data.


### 3 endpoints: 

### * token authorization
      * return token for user after inputed login and password (without case of refresh token after end of his validity)


### * input/creation CBU table
      * recive stricted format of table
      * validate values
      * save data if validation passed wel else return 400 status with reason


### * shows user's saved CBU records 
      * output data or empty array if user still have not records


### * Technologies:
       * Django
       * Django restframework
       * Data base - SQLite, Postgres and etc.


#### Before usage applications: For working with app You need to connect modules from requirements.txt
#### with command in terminal: pip install -r requirements.txt
