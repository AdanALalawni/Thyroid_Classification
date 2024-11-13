# Thyroid_Classification
API for deploy thyroid classifier in this project I deploy thyroid classifier using Restful API that build using FastAPI.
## To build Docker image I write the docker file and in terminal I use this command:
    docker build -t adenal/theroid_classification:v1.0 .
In docke desktop I see that image created successfully

![Alt](https://github.com/AdanALalawni/Thyroid_Classification/blob/main/images/Screenshot%202024-11-13%20151507.png)

To run image I write this command in terminal:

    docker run -p 8000:8000 adenal/theroid_classification:v1.0
In docker desktop I see see the runed Container
![Alt](https://github.com/AdanALalawni/Thyroid_Classification/blob/main/images/Screenshot%202024-11-13%20152157.png)
I check if the API run correctly
![Alt](https://github.com/AdanALalawni/Thyroid_Classification/blob/main/images/Screenshot%202024-11-13%20152235.png)
To push the image to docker hub first I login in docker hub using this command:

    docker login
enter my username and password after that I write this command:
      
    docker push adenal/theroid_classification:v1.0
Go to my docker hub to check if the image pushed 
![Alt](https://github.com/AdanALalawni/Thyroid_Classification/blob/main/images/Screenshot%202024-11-13%20151900.png)

[Link to my Image ]( https://gaganpreetkaurkalsi.netlify.app/](https://hub.docker.com/r/adenal/theroid_classification/tags)
