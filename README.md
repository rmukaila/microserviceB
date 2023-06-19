# microserviceB
git@github.com:rmukaila/microserviceB.git

# How to run app with docker

### Prerequisits for running with docker
### Make sure docker desktop is installed

- Clone the repository with either https link (depends on your git configuration):

    #shell command:

        with ssh link (depends on your git configuration):

        git clone git@github.com:rmukaila/microserviceB.git
       

- cd into the repository folder, create the environment for the project
#shell commands:

        1) cd microserviceB
        2) docker image build -t microserviceB .
        3) docker run -p 5011:5011 -d microserviceB

        
        ##NOTE: Do not omit the dot "." at the end of command 2 above.

- That's it!
    Now headover to start microservice A before testing everythin
