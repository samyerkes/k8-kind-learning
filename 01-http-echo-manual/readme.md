# Manually deploy the http-echo container

## Goal

Deploy a cluster, namespace, deployment, service and ingress on a Kind Kubernetes cluster.

## Steps

Create a cluster:

(Use the yaml file to specify the cluster name and additional ingress related configuration)
```
kind create cluster --config ../my-cluster.yaml
```

Create the ingress for Kind:
```
../ingress-setup.sh
```

Create the namespace and change into it:

(If you don't use kubens you'd have to use `--namespace=my-namespace` on all commands)
```
kubectl apply -f ../my-namespace.yaml
kubens
kubens my-namespace
```

Create the deployment, service and ingress:
```
kubectl apply -f http-echo.yaml
```

Test that everything was deployed correctly:
```
kubectl get pods
kubectl get deployments
kubectl get services

# or

kubectl get all

curl http://localhost
```

Destroy everything:
```
kubectl delete all --all
kubectl delete ingress echo-ingress
kind delete cluster --name my-cluster
```
