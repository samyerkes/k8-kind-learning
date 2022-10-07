# Manually deploy the http-echo container

## Goal

Deploy the http-echo service on a Kind cluster using helm. Then update the helm deployment with new values.

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

Ensure you have the [helm repo installed][echo-server-helm] on your local machine:
```
helm repo add ealenn https://ealenn.github.io/charts
helm repo update
```

Deploy the helm chart:
```
helm install --set ingress.enable=true echo-server ealenn/echo-server
```

Update the helm chart with new values:
```
helm upgrade -i -f ./helm-echo-server.values.yaml echo-server ealenn/echo-server --force
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
helm uninstall echo-server
kind delete cluster --name my-cluster
```

[echo-server-helm]:https://github.com/Ealenn/Echo-Server#kubernetes-with-helm
