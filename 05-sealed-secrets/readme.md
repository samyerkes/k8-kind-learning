# Using Sealed Secrets

## Goal

Deploy a single pod workload that uses a sealed secret set as an environment variable. For demo purposes, the secret will ultimately be displayed on the homepage of the app container.

This sealed secret could be included in version control because only someone who has access to the cluster could decrypt it.

## Steps

Ensure you have installed the kubeseal cli tool:
```
brew install kubeseal
```

Create a cluster:

(Use the yaml file to specify the cluster name and additional ingress related configuration)
```
kind create cluster --config ../my-cluster.yaml
../ingress-setup.sh
```

Create the namespace and change into it:
```
kubectl apply -f ../my-namespace.yaml && kubens my-namespace
```

Install the sealed secrets custom resource into the cluster via helm:
```
helm install sealed-secrets sealed-secrets/sealed-secrets
```

Create the sealed sealed secret and apply it to the cluster:
```
kubectl create secret generic my-secret --dry-run=client --from-literal=SECRET_PHRASE="Not so secret anymore..." -o yaml | \
    kubeseal \
      --controller-name=sealed-secrets \
      --controller-namespace=my-namespace \
      --format yaml > my-sealedsecret.yaml
kubectl apply -f my-sealedsecret.yaml
```

Build the app container and load it in to the cluster:
```
docker build -t not-so-secret container/
kind load docker-image not-so-secret --name my-cluster
docker exec -it my-cluster-worker crictl images | grep not-so-secret
```

Apply the pod and service to the cluster:
```
kubectl apply -f not-so-secret.kube.yaml
```

Verify everything worked correctly:
```
curl http://localhost
kubectl get secrets
kubectl get secret my-secret -o jsonpath="{.data}"
```

Destroy everything:
```
kubectl delete all --all
kind delete cluster --name my-cluster
```
