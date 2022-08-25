# Promethus metrics

## Goal

Gather cluster metrics via Prometheus. In this example we'll install the kube-prometheus-stack via helm. Once installed, you should be able to see the metrics in the Lens UI.

## Steps

Create a cluster:
```
kind create cluster --config ../my-cluster.yaml
```

Create a new namespace for metrics, for this example you can just do this without an extra yaml file:
```
kubectl create namespace metrics
```

Install the Prometheus repo:
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack -n metrics
```

Test that everything was deployed correctly. Also check out the metrics in the Lens UI.
```
kubectl get all -n metrics
```

Destroy everything:
```
kind delete cluster --name my-cluster
```
