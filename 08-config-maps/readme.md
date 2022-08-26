# ConfigMaps

A ConfigMaps allows you to decouple environment-specific configuration from your container images, so that your applications are easily portable.

## Goal

Deploy a container that reads environment variables from a ConfigMap.

## Steps

Create a cluster:
```
kind create cluster --config ../my-cluster.yaml && ../ingress-setup.sh && kubectl apply -f ../my-namespace.yaml
```

Create the ConfigMap and apply it (note that this will override the ConfigMap that is saved in the repo):
```
k create configmap my-configmap --dry-run=client --output yaml > my-configmap.yaml 
```

Create the container image and load the image into the Kind cluster:
```
docker build -t hello-config-map container/
kind load docker-image hello-config-map --name my-cluster
```

Check the container has been loaded into the cluster:
```
docker exec -it my-cluster-worker crictl images | grep hello-config-map
```

Create the deployment, service and ingress:
```
kubectl apply -f my-app.kube.yaml
```

Test that everything was deployed correctly:
```
curl http://localhost
```

Destroy everything:
```
kind delete cluster --name my-cluster
```
