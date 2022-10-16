# Test Plan
This file records the test plan for [`main.py`](/Backend/main.py). Ordered by operation, table.
* POST
    * [User](#operation-apppostuser-response_modelschemasuser) 
    * [Task](#operation-appposttask-response_modelschemastask)
* GET
    * [User](#operation-appgetuseruser_id-response_modelschemasuser)
    * [Task](#operation-appgettasktask_id-response_modelschemastask)
* PUT 
    * [User](#operation-appputuseruser_id-response_modelschemasuser)
    * [Task](#operation-appputtasktask_id-response_modelschemastask)
* DELETE
    * [User](#operation-appdeleteuseruser_id)
    * [Task](#operation-appdeletetasktask_id)

## POST
### Operation: @app.post("/user/", response_model=schemas.User)
|Test|Inputs|Expected Outcome|Test Outcome|Result|Changes|
|:--:|------|----------------|------------|------|-------|
|1|{"name": "fake user", "email": "test@test.com", "password": "NoProtectionPassword"}|{"name": "fake user","email": "test@test.com","id": 1,"has_task": []}|{"name": "fake user","email": "test@test.com","id": 1,"has_task": []}|Pass||
|2|{"name": "exist user", "email": "test@test.com", "password": "AnotherNoProtectionPassword"}|400 Bad Request {"detail": "User exist"}|400 Bad Request {"detail": "User exist"}|Pass||


### Operation: @app.post("/task/", response_model=schemas.Task)
|Test|Inputs|Expected Outcome|Test Outcome|Result|Changes|
|:--:|------|----------------|------------|------|-------|
|1|{"name": "add test","ddl_time": "2022-10-16T20:20Z","user_id": 1}|<mark> 404 Not Found </mark>{ "detail": "User not found, cannot insert"}|~~500 Internal Server Error~~|Fail|Fixed not to catch all exceptions at *except* part |
|2|{"name": "add test","ddl_time": "2022-10-16T20:20Z","user_id": 1}|{"name": "add test","ddl_time": "2022-10-16T21:20:00+01:00","id": 1,"create_time": "2022-10-13T21:33:20.437018+01:00"}|{"name": "add test","ddl_time": "2022-10-16T21:20:00+01:00","id": 1,"create_time": "2022-10-13T21:33:20.437018+01:00"}|Pass||
|3|{"name": "add test","ddl_time": "2022-10-16T20:20Z","user_id": 7}|404 Not Found { "detail": "User not found, cannot insert"}|404 Not Found { "detail": "User not found, cannot insert"}|Pass||

## GET
### Operation: @app.get("/user/{user_id}", response_model=schemas.User)
|Test|Inputs|Expected Outcome|Test Outcome|Result|Changes|
|:--:|------|----------------|------------|------|-------|
|1|1|{"name":"fake user","email":"test@test.com","id":1,"has_task":<mark>[{"name":"add test","ddl_time":"2022-10-16T21:20:00+01:00","user_id":1,"id":1,"create_time":"2022-10-13T21:33:20.437018+01:00"}]</mark>}|{"name":"fake user","email":"test@test.com","id":1,"has_task":~~[ ]~~}|Fail|schema has attribute name as *has_task*, where models has column *has_tasks*, changed both as **has_tasks**|
|2|1|{"name": "update name","email": "string","id": 1,"has_tasks": [{"name": "task2","ddl_time": "2022-10-20T21:53:29.496000+01:00","user_id": 1},{"name": "task3","ddl_time": "2022-10-21T21:53:29.496000+01:00","user_id": 1},{"name": "update task","ddl_time": "2022-10-30T21:33:36.857000+00:00","user_id": 1}]}|{"name": "update name","email": "string","id": 1,"has_tasks": [{"name": "task2","ddl_time": "2022-10-20T21:53:29.496000+01:00","user_id": 1},{"name": "task3","ddl_time": "2022-10-21T21:53:29.496000+01:00","user_id": 1},{"name": "update task","ddl_time": "2022-10-30T21:33:36.857000+00:00","user_id": 1}]}|Pass||

### Operation: @app.get("/task/{task_id}", response_model=schemas.Task)
|Test|Inputs|Expected Outcome|Test Outcome|Result|Changes|
|:--:|------|----------------|------------|------|-------|
|1|1|{"name":"add test","ddl_time":"2022-10-16T21:20:00+01:00","user_id":1,"id":1,"create_time":"2022-10-13T21:33:20.437018+01:00"}|{"name":"add test","ddl_time":"2022-10-16T21:20:00+01:00","user_id":1,"id":1,"create_time":"2022-10-13T21:33:20.437018+01:00"}|Pass||

## PUT
### Operation: @app.put("/user/{user_id}", response_model=schemas.User)
|Test|Inputs|Expected Outcome|Test Outcome|Result|Changes|
|:--:|------|----------------|------------|------|-------|
|1|1 {"name": "update name", "email": "test@test.com", "password": "AnotherNoProtectionPassword"}|{"name": "update name","email": "test@test.com","id": 1,"has_tasks": [{"name": "task2","ddl_time": "2022-10-20T21:53:29.496000+01:00","user_id": 1},{"name": "task3","ddl_time": "2022-10-21T21:53:29.496000+01:00","user_id": 1},{"name": "update","ddl_time": "2022-10-16T23:05:48.025000+01:00","user_id": 1}]}|{"name": "update name","email": "test@test.com","id": 1,"has_tasks": [{"name": "task2","ddl_time": "2022-10-20T21:53:29.496000+01:00","user_id": 1},{"name": "task3","ddl_time": "2022-10-21T21:53:29.496000+01:00","user_id": 1},{"name": "update","ddl_time": "2022-10-16T23:05:48.025000+01:00","user_id": 1}]}|Pass||
|2|1 {"name": "update name2", "email": "test@test.com", "password": "AnotherNoProtectionPassword"}|{"name": "update name2","email": "test@test.com","id": 1,"has_tasks": [{"name": "task2","ddl_time": "2022-10-20T21:53:29.496000+01:00","user_id": 1},{"name": "task3","ddl_time": "2022-10-21T21:53:29.496000+01:00","user_id": 1},{"name": "update","ddl_time": "2022-10-16T23:05:48.025000+01:00","user_id": 1}]}|400 Bad Request {"detail": "This email already linked with another account"}|Fail|Fixed the email check to `if select_user != this_user`|
|3|1 {"name": "update name2", "email": "test@test.com", "password": "AnotherNoProtectionPassword"}|{"name": "update name2","email": "test@test.com","id": 1,"has_tasks": [{"name": "task2","ddl_time": "2022-10-20T21:53:29.496000+01:00","user_id": 1},{"name": "task3","ddl_time": "2022-10-21T21:53:29.496000+01:00","user_id": 1},{"name": "update","ddl_time": "2022-10-16T23:05:48.025000+01:00","user_id": 1}]}|{"name": "update name2","email": "test@test.com","id": 1,"has_tasks": [{"name": "task2","ddl_time": "2022-10-20T21:53:29.496000+01:00","user_id": 1},{"name": "task3","ddl_time": "2022-10-21T21:53:29.496000+01:00","user_id": 1},{"name": "update","ddl_time": "2022-10-16T23:05:48.025000+01:00","user_id": 1}]}|Pass||

### Operation: @app.put("/task/{task_id}", response_model=schemas.Task)
|Test|Inputs|Expected Outcome|Test Outcome|Result|Changes|
|:--:|------|----------------|------------|------|-------|
|1|1 {"name": "update task","ddl_time": "2022-10-30T21:33:36.857000+00:00","user_id": 1}|{"name": "update task","ddl_time": "2022-10-30T21:33:36.857000+00:00","user_id":1,"id":1,"create_time":"2022-10-13T21:33:20.437018+01:00"}|{"name": "update task","ddl_time": "2022-10-30T21:33:36.857000+00:00","user_id":1,"id":1,"create_time":"2022-10-13T21:33:20.437018+01:00"}|Pass||
|2|1 {"name": "user not exist","ddl_time": "2022-10-30T21:33:36.857000+00:00","user_id": 0}|404 Not Found{"detail": "User not found"}|404 Not Found{"detail": "User not found"}|Pass||

## DELETE
### Operation: @app.delete("/user/{user_id}")
|Test|Inputs|Expected Outcome|Test Outcome|Result|Changes|
|:--:|------|----------------|------------|------|-------|
|1|1|{"Delete": "True"}|{"Delete": "True"}|Pass||
|2|10|404 Not Found { "detail": "Task not found"}|404 Not Found{"detail": "Task not found"}|Pass||

### Operation: @app.delete("/task/{task_id}")
|Test|Inputs|Expected Outcome|Test Outcome|Result|Changes|
|:--:|------|----------------|------------|------|-------|
|1|3|{"Delete": "True"}|{"Delete": "True"}|Pass||
|2|30| 404 Not Found { "detail": "Task not found"}|404 Not Found{"detail": "Task not found"}|Pass||