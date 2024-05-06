# GitlabPOC

## Description

This is a POC for using Gitlab to create and monitor software pipelines.

At the time of this writing, the pipeline is designed to excercise a number of GitLab features in a very basic manner: 

- Build a basic hello world web service written in python (bare bones)
- Lint the code
- Run unit tests
- Install python modules from the GitLab package Registry
- Use the GitLab container registry
- Push the simple_server code docker image to the GitLab container registry

## Notes 

The build is done using the most recent locally (to GitLab) available docker image from the runner, but it could also point to latest rather than the pinned version: registry.sh.nextgenwaterprediction.com/infrastructure/docker/docker:26.0.2 
