# Iris classification service

This project trains a logistic-regression classifier on the built-in Iris data set and exposes it through a Flask API.

## Run locally

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python train_model.py
python score.py
```

Call `POST /predict` with `{"features": [5.1, 3.5, 1.4, 0.2]}`. `GET /health` is the container health endpoint.

## GitHub Actions deployment

The workflow tests the application, builds an image, pushes it to Azure Container Registry (ACR), then deploys `aks.yaml` to AKS. It runs on pushes to `master` and can also be started manually.

Before its first run, create an AKS cluster and ACR (or reuse existing ones), attach ACR to AKS, and configure OpenID Connect federated credentials for a Microsoft Entra application. The identity needs `AcrPush` on ACR and permission to deploy to AKS. Add these repository secrets:

- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

Add these repository variables:

- `ACR_NAME` — registry name only, for example `manjularegistry`
- `AZURE_RESOURCE_GROUP` — AKS resource group
- `AKS_CLUSTER` — AKS cluster name

The Kubernetes cluster must be able to pull the ACR image; `az aks update --attach-acr <acr-name>` configures that relationship for a compatible cluster identity.
