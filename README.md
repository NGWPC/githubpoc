# GitlabPOC

## Description

This is a POC for using Gitlab to create and monitor software pipelines.

At the time of this writing, the pipeline is designed to: 

- Push to "production" and "staging" environments
- Build and push a Rocky Linux 9 image to the Gitlab repository
- Require manual approval in the Gitlab dashboard to "deploy"

## Issues 

Issues encountered that might need to be overcome prior to using this solution:

- I ran into issues accessing the Gitlab via SSH and used the web IDE to complete this POC.
- Docker builds do not appear to be possible yet- it appears Docker may not be installed/ running on the instance Gitlab is on. This would be an easy fix, but for the meantime, this pipeline is running faux builds.