import os

# repo_folder = os.environ.get('$REPO_NAME', 'REPO_NAME')
image_name = os.environ['IMAGE_NAME']
pod_name = os.environ['APP_POD_NAME']
serive_name = os.environ['APP_SERVICE_NAME']
db_pod_name = os.environ['DB_POD_NAME']
db_serive_name = os.environ['DB_SERVICE_NAME']
sub_domain = os.environ['SUB_DOMAIN']
odoo_version = os.environ['ODOO_VERSION']
# repository_uri = os.environ['repository_uri']

# dockerfile_content = f"""

# FROM ubuntu:22.04

# USER root

# ENV DEBIAN_FRONTEND=noninteractive \
#     LANG=C.UTF-8
    

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     python3 \
#     python3-pip \
#     python3-wheel \
#     libxrender-dev \
#     libxext-dev \
#     libfontconfig1 \
#     libfreetype6 \
#     fontconfig \
#     git-core \
#     gcc \
#     g++

# RUN apt-get install -y python3-dev libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev

# RUN apt install postgresql-client -y

# WORKDIR /opt/odoo

# COPY ./repo_code .

# RUN pip3 install -r  requirements.txt
# CMD ["./odoo-bin", "-c", "/opt/odoo/config/odoo.conf"]
# """

dockerfile_content = f"""
FROM odoo:{odoo_version}

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


postgres_pod_yml_content = f"""
apiVersion: v1
kind: Pod
metadata:
  name: {db_pod_name}
  labels:
    app.kubernetes.io/name: {db_pod_name}
spec:
  containers:
  - name: {db_pod_name}
    image: postgres:14
    ports:
    - containerPort: 5432
    env:
    - name: POSTGRES_DB
      value: postgres
    - name: POSTGRES_PASSWORD
      value: odoo
    - name: POSTGRES_USER
      value: odoo
    - name: PGDATA
      value: /var/lib/postgresql/data/pgdata
    """

        
with open("postgres-pod.yml", "w") as pp_writer:
    pp_writer.write(postgres_pod_yml_content)

# postgres_service_yml_content = """
# apiVersion: v1
# kind: Service
# metadata:
#   name: postgres-service2
# spec:
#   type: NodePort
#   selector:
#     app.kubernetes.io/name: postgres-db2
#   ports:
#     - protocol: TCP
#       port: 5432
#       targetPort: 5432
#       nodePort: 31002
# """ 
postgres_service_yml_content = f"""
apiVersion: v1
kind: Service
metadata:
  name: {db_serive_name}
spec:
  selector:
    app.kubernetes.io/name: {db_pod_name}
  ports:
    - protocol: TCP
      port: 5432
      targetPort: 5432
""" 
with open("postgres-service.yml", "w") as ps_writer:
    ps_writer.write(postgres_service_yml_content)


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
    ports:
    - containerPort: 8000
  imagePullSecrets:
  - name: regcred
    """
        
with open("odoo-pod.yml", "w") as op_writer:
    op_writer.write(odoo_app_pod_yml_content)


# odoo_app_service_yml_content = """
# apiVersion: v1
# kind: Service
# metadata:
#   name: odoo-service2
# spec:
#   type: NodePort
#   selector:
#     app.kubernetes.io/name: odoo-app2
#   ports:
#     - protocol: TCP
#       port: 8069
#       targetPort: 8069
#       nodePort: 31003
#     """

# odoo_app_service_yml_content = f"""
# apiVersion: v1
# kind: Service
# metadata:
#   name: {serive_name}
# spec:
#   type: LoadBalancer
#   selector:
#     app.kubernetes.io/name: {pod_name}
#   ports:
#     - protocol: TCP
#       port: 8069
#       targetPort: 8069
#     """

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

ingress_rule_content = f"""
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-rules-for-{serive_name}
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: "100m"
  namespace: default
spec:
  ingressClassName: nginx-class
  rules:
  - host: "{sub_domain}.erp-deploy.com"
    http:
      paths:
      - backend:
          service:
            name: {serive_name}
            port:
              number: 8069
        path: /
        pathType: ImplementationSpecific
"""
with open("ingress-rule.yml", "w") as ir_writer:
    ir_writer.write(ingress_rule_content)
