# Use GitOps with Flux

## Goal

Apply a deployment, service and namespace automatically via GitOps with [Flux](https://fluxcd.io). Completing these steps will deploy the same resources found in `01-http-echo-manual`.

## Steps

Ensure you have the Flux CLI installed:
```
brew install fluxcd/tap/flux
```

This demo will use Github, so export your Github personal access token and username:
```
export GITHUB_TOKEN=<your-token>
export GITHUB_USER=<your-username>
```

Create a cluster:

(Use the yaml file to specify the cluster name and additional ingress related configuration)
```
kind create cluster --config ../my-cluster.yaml && ../ingress-setup.sh
```

Check if you have everything installed  correctly:
```
flux check --pre
```

Install Flux into your cluster, setting it to look at this repository and path. If the Github repo doesn't exist it will create it. As Flux is installed into the repo it will apply manifests that it finds to the cluster.
```
flux bootstrap github \
  --owner=$GITHUB_USER \
  --repository=k8-kind-flux-demo-monorepo \
  --branch=main \
  --path=./clusters/my-cluster \
  --personal
```

Test that everything was deployed correctly:
```
kubectl get pods -n my-namespace
kubectl get deployments -n my-namespace
kubectl get services -n my-namespace

# or

kubectl get all -n my-namespace

curl http://localhost
```

Destroy everything:
```
kind delete cluster --name my-cluster
```
