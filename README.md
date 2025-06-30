# GitHubPOC

## Description

This is a proof of concept (POC) for using **GitHub Actions** with linux based **self-hosted runners** in NGWPC's AWS environment to run software pipelines.

At the time of this writing, the reference pipeline exercises a number of GitHub Actions features:

- Build a basic "Hello World" web service written in Python
- Lint the code using `flake8`
- Run unit tests with coverage reporting
- Perform static code analysis using **SonarQube**
- Build and push Docker images to the **GitHub Container Registry (GHCR)**
- Perform container vulnerability scanning using **Trivy**
- Deploy / Push the image with semantic version and `latest` tags (on push to `main`) in the **GitHub Container Registry (GHCR)**

If in the future we can identify reusable workflow stages, we can add a repo for them and update examples to leverage something like:
    
    uses: ngwpc/github-actions-workflows/.github/workflows/reusablestagename.yaml@main

## Pipeline Stages

### 1. **Lint**
Runs `flake8` in a Rocky Linux container to ensure code quality and style compliance.

### 2. **Unit Tests**
Executes tests with `pytest`, generates coverage reports, and saves results as artifacts.

### 3. **SonarQube Scan**
Uses `sonarsource/sonar-scanner-cli` to analyze code quality, referencing test and coverage results from the previous step.

### 4. **Build**
- Uses `docker/buildx` to build the Docker image.
- Pushes the image to the **GitHub Container Registry (GHCR)** under the format: ghcr.io/ngwpc/simple_server:branch-name

### 5. **Container Scanning**
- Pulls the newly built image.
- Runs **Trivy** to detect vulnerabilities.
- Uploads results as SARIF if the repository is public.

### 6. **Deploy**
- Executes only on pushes to the `main` branch.
- Pulls and tags the image with `latest` and a static version (e.g., `0.0.1`).
- Pushes both tags to GHCR.

## Notes

- The workflow is defined in `.github/workflows/ci-cd.yaml`.
- The pipeline relies on **self-hosted GitHub runners** running containers based on Rocky Linux.
- Secrets such as `SONAR_HOST_URL`, `SONAR_TOKEN` have been set for the Organization and are required for full functionality.
- Trivy uploads are gated to public repos due to SARIF support only being available in GitHub with extra paid Advanced Security features enabled.

## Previous GitLab Setup

This project was originally built using GitLab CI/CD and GitLab Container Registry. It has been ported to GitHub as part of a broader transition. The original `.gitlab-ci.yml` exercised similar functionality, targeting GitLab-native tooling and registries.  This has been retained in the repo for reference.
