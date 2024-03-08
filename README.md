# GitlabPOC

## Description

This is a POC for using Gitlab to create and monitor software pipelines.

At the time of this writing, the pipeline is designed to: 

- Push to "production" and "staging" environments
- Build and push a Rocky Linux 9 image to the Gitlab repository
- Require manual approval in the Gitlab dashboard to "deploy"

## Notes

Currently, this pipeline does not actually build an image. The Dockerfile was added for potential future testing. 

## Issues 

Issues encountered that might need to be overcome prior to using this solution:

- Docker builds do not appear to be possible yet- it appears Docker may not be installed/ running on the instance Gitlab is on. This would be an easy fix, but for the meantime, this pipeline is running faux builds.