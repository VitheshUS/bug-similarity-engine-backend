We have used Clean architeture
    API - endpoints,dependency injection
    APPLICATION - business logic
    DOMAIN - rules and models like validation, exception and other models
    INFRASTRUCTURE - data,model,index this includes all the opertion that untilzez system resource

We have initialized the fast API in the API layer
We have used logger for logging
Context lib for managing resource, here we have used contextmanager of fastAPI and we are doing model,index initialize as well
We are also observing the time taken to embed,transform,fetch using time and logging it, this will help us to debug in production

We have written exception which will be thrown, we have fastAPI exception handler
Exceptio handler we define the type of exception that will capture, its just like registering the endpoints