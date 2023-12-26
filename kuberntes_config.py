import os

# repo_folder = os.environ.get('$REPO_NAME', 'REPO_NAME')
image_name = os.environ['IMAGE_NAME']

dockerfile_content = f"""

FROM ubuntu:22.04


USER root

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8
    

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-wheel \
    libxrender-dev \
    libxext-dev \
    libfontconfig1 \
    libfreetype6 \
    fontconfig \
    git-core \
    gcc \
    g++

RUN apt-get install -y python3-dev libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev


WORKDIR /opt/odoo

COPY ./repo_code .

RUN pip3 install -r  requirements.txt
CMD ["./odoo-bin", "-c", "/opt/odoo/config/odoo.conf"]
"""


dockerfile_path = "Dockerfile"
with open(dockerfile_path, "w") as dockerfile:
    dockerfile.write(dockerfile_content)


postgres_pod_yml_content = """
apiVersion: v1
kind: Pod
metadata:
  name: postgres-db
  labels:
    app.kubernetes.io/name: postgres-db
spec:
  containers:
  - name: postgres
    image: postgres:15
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
#   name: postgres-service
# spec:
#   type: NodePort
#   selector:
#     app.kubernetes.io/name: postgres-db
#   ports:
#     - protocol: TCP
#       port: 5432
#       targetPort: 5432
#       nodePort: 31000
# """       
# with open("postgres-service.yml", "w") as ps_writer:
#     ps_writer.write(postgres_service_yml_content)

postgres_service_yml_content = """
apiVersion: v1
kind: Service
metadata:
  name: postgres-service
spec:
  selector:
    app.kubernetes.io/name: postgres-db
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
  name: odoo-app
  labels:
    app.kubernetes.io/name: odoo-app
spec:
  containers:
  - name: odoo-app
    image: {image_name}
    ports:
    - containerPort: 8000
    """
        
with open("odoo-pod.yml", "w") as op_writer:
    op_writer.write(odoo_app_pod_yml_content)


odoo_app_service_yml_content = """
apiVersion: v1
kind: Service
metadata:
  name: odoo-service
spec:
  type: NodePort
  selector:
    app.kubernetes.io/name: odoo-app
  ports:
    - protocol: TCP
      port: 8069
      targetPort: 8069
      nodePort: 31001
    """
        
with open("odoo-service.yml", "w") as os_writer:
    os_writer.write(odoo_app_service_yml_content)
