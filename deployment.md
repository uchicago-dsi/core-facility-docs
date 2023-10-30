## Deploying to Google Cloud Using GitHub Actions

A common thing you might want to do is upload a Docker image to Google Artifact Registry whenever you update a specific branch like `dev` or `main`.

You can set this up using GitHub actions, although the configuration can be a little bit tricky.

To set up a GitHub action, create a `.yml` file in `.github/workflows` for your repo. [This documentation](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) explains the overall structure of a GitHub action.

Here's an example of a working (as of October 2023) deployment action `.yml` file:
```
name: Deploy to Google Artifact Registry

on:
  push:
    branches:
      - dev

jobs:
  build-and-push:
    # environment is created and variables are stored in GitHub settings for the repo
    # access variables with syntax: ${{ vars.VARIABLE_NAME }}
    environment: "Climate Cabinet"
    runs-on: ubuntu-latest

    # Add "id-token" with the intended permissions. Used for OIDC connection with GitHub
    permissions:
      contents: read
      id-token: write

    steps:
      # Needs to be run before "auth" action
      - uses: actions/checkout@v3

      # Use OIDC authentication to get an access token from GitHub
      - id: auth
        name: "Authenticate to Google Cloud"
        uses: google-github-actions/auth@v1
        with:
          workload_identity_provider: ${{ vars.WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ vars.ARTIFACT_SERVICE_ACCOUNT }}
          token_format: access_token

      # Login with Docker action using the token from the Google Cloud auth step
      - uses: docker/login-action@v3
        with:
          registry: ${{ vars.CLOUD_REGION }}
          username: oauth2accesstoken
          password: ${{ steps.auth.outputs.access_token }}

      - id: "docker-push-tagged"
        name: "Tag Docker image and push to Google Artifact Registry"
        uses: docker/build-push-action@v5
        with:
          push: true
          context: ./pipeline
          file: ./pipeline/Dockerfile
          tags: ${{ vars.CLOUD_REGION }}/${{ vars.PROJECT_ID }}/${{ vars.ARTIFACT_REPOSITORY }}/${{ vars.IMAGE_TAG }}:latest

```

A few things to note:
- The action will run on GitHub, so you need to [set up environment variables for your project on GitHub](https://docs.github.com/en/actions/learn-github-actions/variables). These are accessed with the syntax `${{ vars.VARIABLE_NAME }}`
- Google has switched to [federated identity verification](https://cloud.google.com/iam/docs/workload-identity-federation). This can be confusing because there are a lot of examples on the web that use a previous authorization method that doesn't work anymore. In order to authenticate with Google Cloud, you need to [set up your GitHub account to be able to get access tokens for Google Cloud](https://cloud.google.com/blog/products/identity-security/enabling-keyless-authentication-from-github-actions). Then, you need to pass that token on to the following steps - this is what the `${{ steps.auth.outputs.access_token }}` is doing for the `docker/login-action@v3` step. Make sure you've also given the token adequate permissions — check the `permissions` section of the `.yml` file for an example.
- There are a lot of prebuilt actions setup for Docker and GitHub actions. You can [take a look at them here](https://docs.docker.com/build/ci/github-actions/).
- You will need to get your cloud region, project_id, and artifact repository from Google Cloud. You can copy this directly from Google Artifact Registry and it will look something like this: `us-central1-docker.pkg.dev/climate-cabinet-398217/ira-pipeline`