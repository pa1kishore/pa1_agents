
Install and initialize the Google Cloud CLI: Follow the instructions to install the gcloud CLI and run gcloud init to set up your project and authenticate.
Enable necessary APIs: Ensure the Cloud Run and Artifact Registry APIs are enabled for your project.
bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
Use code with caution.

Build the Docker image and push to Artifact Registry:
Create a Docker repository in Artifact Registry if you don't have one:
bash
gcloud artifacts repositories create docker-repo --repository-format=DOCKER --location=us-east4 --description="Docker repository"
Use code with caution.

Build and push the image to the registry (replace us-east4 and lexical-helix-462005-m6 with your specifics):
bash
# Define image path
IMAGE_URL="us-east4-docker.pkg.dev/lexical-helix-462005-m6/docker-repo/excel-processor:v1"

# Build the container image
gcloud builds submit --tag $IMAGE_URL .
Use code with caution.

Deploy to Cloud Run:
Deploy the container image to Cloud Run. You may allow unauthenticated access for simplicity during the quickstart.
bash
gcloud run deploy excel-processor-service --image $IMAGE_URL --platform managed --region us-east4 --allow-unauthenticated
Use code with caution.

Test the Deployment:
Once the deployment is complete, the gcloud CLI will provide a Service URL. You can use a tool like curl or Postman to test the endpoint.
Example using curl (replace <SERVICE_URL> with your actual URL):
bash
curl -X POST <SERVICE_URL>/upload-excel/ \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/local/file.xlsx" \
  -F "user_id=testuser123" \
  -F "description=A sample file upload test"
Use code with caution.

This will return a JSON response with the processing details

gcloud projects add-iam-policy-binding lexical-helix-462005-m6 \
    --member="serviceAccount:908887859066-compute@developer.gserviceaccount.com" \
    --role="roles/storage.objectAdmin"


### Build
gcloud builds submit --tag us-east4-docker.pkg.dev/lexical-helix-462005-m6/docker-repo/excel-processor:v1 .
### Deploy and Run
gcloud run deploy excel-processor-service --image us-east4-docker.pkg.dev/lexical-helix-462005-m6/docker-repo/excel-processor:v1 --platform managed --region us-east4 --allow-unauthenticated