FROM jupyterhub/jupyterhub:0.9.4

RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py

RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0

COPY jupyterhub_config.py .
