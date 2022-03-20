kubectl delete -n argo cm aws-artifacts
kubectl delete -n argo secret tks-admin-kubeconfig-secret

kubectl create -n argo cm aws-artifacts --from-file=artifacts
kubectl create -n argo secret generic tks-admin-kubeconfig-secret --from-file=value=${HOME}/.kube/config

kubectl create -n argo secret generic awsconfig-secret --from-file=config=awsconfig/config --from-file=credentials=awsconfig/credentials