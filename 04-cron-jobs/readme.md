# Cron Jobs

## Goal

Deploy a cluster that has a custom automated job running on a cron.

## Steps

Create a cluster:

(Use the yaml file to specify the cluster name and additional ingress related configuration)
```
kind create cluster --config ../my-cluster.yaml
```

Create the namespace and change into it:

(If you don't use kubens you'd have to use `--namespace=my-namespace` on all commands)
```
kubectl apply -f ../my-namespace.yaml && kubens my-namespace
```

Build the job container and load it in to the cluster:
```
docker build -t my-job container/
kind load docker-image my-job --name my-cluster
docker exec -it my-cluster-worker crictl images | grep my-job
```

Create a new cronJob skeleton to edit (note, this will override the example):
```
kubectl create cronjob my-job --image=docker.io/library/my-job --schedule="* * * * *" --dry-run=client -o yaml > my-cronjob.yaml
```

Create the cronJob:
```
kubectl apply -f my-cronjob.yaml
```

Test that everything was applied correctly:
```
kubectl get cronjobs -o wide
kubectl get jobs
kubectl logs -l job=my-job --all-containers=true
```

Destroy everything:
```
kubectl delete all --all
kind delete cluster --name my-cluster
```
