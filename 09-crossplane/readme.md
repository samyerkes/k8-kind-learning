# Crossplane

Crossplane is a CNCF sponsored project that allow you to provision infrastructure via the Kubernetes api. It is a way of doing infrastructure as code similar to Terraform or Cloudformation, but through a Kubernetes cluster. Paired with a git ops approach it becomes extremely powerful since developers then only need to focus on understanding Kubernetes and not individual cloud providers.

## Goal

Deploy a S3 bucket to AWS via Crossplane.

## Steps

Create a cluster:
```
kind create cluster --config ../my-cluster.yaml
```

Install Crossplane via a Helm chart:
```
helm repo add crossplane-stable https://charts.crossplane.io/stable && helm repo update

helm install crossplane crossplane-stable/crossplane --namespace crossplane-system --create-namespace
```

Verify Crossplane has been properly installed:
```
kubectl get pods -n crossplane-system
helm list -n crossplane-system
```

Install the AWS provider:
```
kubectl apply -f crossplane-aws-provider.yaml
```

In AWS create a new user with cli access key. Ensure the user has the appropriate policy to grant permissions as needed; for this example you can temporarily add the AmazonS3FullAccess AWS managed policy. Add the key id and secret to aws-credentials.txt.

Create a Kubernetes secret with the AWS Credentials so that Crossplane can provisions resources in the AWS Account.
```
kubectl create secret generic aws-secret -n crossplane-system --from-file=creds=./aws-credentials.txt
```

Create a new Crossplane ProviderConfig that uses the AWS secret made in the previous example.
```
kubectl apply -f crossplane-aws-provider-config.yaml
```

Finally we can create the S3 bucket through a Kubernetes manifest file and apply it with:
```
kubectl apply -f s3-bucket.yaml
```
This will create an S3 bucket prefixed with `crossplane-bucket-` as the name in us-east-1. You can verify this in the AWS console, AWS CLI or with kubectl:
```
kubectl get buckets
```

If someone where to manually delete this bucket Crossplane would reprovision it since it becomes the source of truth.

Destroy the kind cluster and ensure you remove the IAM access granted to Crossplane.
```
kind delete cluster --name my-cluster
```
