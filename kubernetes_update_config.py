import os

image_name = os.environ['IMAGE_NAME']
pod_name = os.environ['APP_POD_NAME']
serive_name = os.environ['APP_SERVICE_NAME']
db_serive_name = os.environ['DB_SERVICE_NAME']



dockerfile_content = f"""
FROM odoo:16

USER root

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8

RUN apt install postgresql-client -y

COPY ./config /etc/odoo
COPY ./custom-addons /mnt/extra-addons/custom-addons
"""

dockerfile_path = "Dockerfile"
with open(dockerfile_path, "w") as dockerfile:
    dockerfile.write(dockerfile_content)



odoo_app_pod_yml_content = f"""
apiVersion: v1
kind: Pod
metadata:
  name: {pod_name}
  labels:
    app.kubernetes.io/name: {pod_name}
spec:
  containers:
  - name: {pod_name}
    image: {image_name}
    imagePullPolicy: Always
    ports:
    - containerPort: 8000
  imagePullSecrets:
  - name: regcred
    """
        
with open("odoo-pod.yml", "w") as op_writer:
    op_writer.write(odoo_app_pod_yml_content)


odoo_app_service_yml_content = f"""
apiVersion: v1
kind: Service
metadata:
  name: {serive_name}
spec:
  selector:
    app.kubernetes.io/name: {pod_name}
  ports:
    - protocol: TCP
      port: 8069
      targetPort: 8069
    """
with open("odoo-service.yml", "w") as os_writer:
    os_writer.write(odoo_app_service_yml_content)
