# How to run this backend code
- Option 1:
    cd to folder `DDL-reminder-App`, then run `uvicorn Backend.main:app --reload`. 
- Option 2:
    cd to folder `Backend`, replace all `from . import xxx` with `import xxx`, then run `uvicorn main:app --reload`.

Where `main` is the file name(`Backend.`with src), `app` is the name of app variable and `— reload` will restart server anytime when make a change to the code and should only be used in development.


## database ORM
For this project, I chose to use **SQLAlchemy** over *PeeWee*. Simply because sqlalchemy don't have to deal with the async-compatible problem as peewee need, and a little bit easier to write codes when need to CRUD with database.