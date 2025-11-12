

1. init uv inside a new empty directory `uv init`  
2. add dependencies  
```bash
uv add langchain python-dotenv black isort
```

3. Get LLM API key



- some important commands:
```bash
# run scripts
uv run main.py

# generate lock file
uv lock

# synv environment
uv sync

# install from txt file
uv pip install -r requirements.txt
```

pip install pip-system-certs



---

```
I0000 00:00:1761083730.435180   25908 ssl_transport_security.cc:1884] Handshake failed with error SSL_ERROR_SSL: error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate
I0000 00:00:1761083730.515274   21072 ssl_transport_security.cc:1884] Handshake failed with error SSL_ERROR_SSL: error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate
I0000 00:00:1761083730.592709   12004 ssl_transport_security.cc:1884] Handshake failed with error SSL_ERROR_SSL: error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate
I0000 00:00:1761083730.672227    1292 ssl_transport_security.cc:1884] Handshake failed with error SSL_ERROR_SSL: error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate
```