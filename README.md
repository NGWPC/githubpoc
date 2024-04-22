# GitlabPOC

## Description

This is a POC for using Gitlab to create and monitor software pipelines.

At the time of this writing, the pipeline is designed to: 

- Push to "production" and "staging" environments
- Build and push a Rocky Linux 9 image to the Gitlab repository
- Require manual approval in the Gitlab dashboard to "deploy"

## Notes 

The build is done using the most recent locally (to GitLab) available docker image from the runner, but it could also point to latest rather than the pinned version: registry.sh.nextgenwaterprediction.com/infrastructure/docker/docker:26.0.2 
