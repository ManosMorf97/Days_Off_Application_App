#!/bin/sh

SRCTMPFILE=$(mktemp /tmp/tmp_ingress_controller.src.XXXXXXXXXXX.yaml)
NEWTMPFILE=$(mktemp /tmp/tmp_ingress_controller.new.XXXXXXXXXXX.yaml)

microk8s kubectl get -ningress daemonset.apps/nginx-ingress-microk8s-controller -o yaml > $SRCTMPFILE
sed -e "s/\(\- \-\-publish-status-address=\).*/\1$(curl ifconfig.io 2>/dev/null)/g" $SRCTMPFILE > $NEWTMPFILE

if [ ! "" = "$(diff -q $NEWTMPFILE $SRCTMPFILE)" ]; then
	echo Updating publish status address
	diff $SRCTMPFILE $NEWTMPFILE
	microk8s kubectl apply -f $NEWTMPFILE
fi

rm $SRCTMPFILE
rm $NEWTMPFILE
