# Manually deploy a custom container

## Goal

Deploy a custom container to the cluster

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
kubectl apply -f ../my-namespace.yaml && kubens my-namespace
```

Create the container image and load the image into the Kind cluster:
```
docker build -t hello-k8 container/
kind load docker-image hello-k8 --name my-cluster
```

Check the container has been loaded into the cluster:
```
docker exec -it my-cluster-worker crictl images | grep hello-k8
```

Create the deployment, service and ingress:
```
kubectl apply -f hello-k8.yaml
```

Test that everything was deployed correctly:
```
curl http://localhost
curl http://localhost/k8
```

Destroy everything:
```
kubectl delete all --all
kubectl delete ingress hello-k8-ingress
kind delete cluster --name my-cluster
```
