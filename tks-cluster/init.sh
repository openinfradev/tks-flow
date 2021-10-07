kubectl delete -n argo cm aws-artifacts
kubectl delete -n argo secret tks-admin-kubeconfig-secret

kubectl create -n argo cm aws-artifacts --from-file=artifacts
kubectl create -n argo secret generic tks-admin-kubeconfig-secret --from-file=value=/home/siim/.kube/config 