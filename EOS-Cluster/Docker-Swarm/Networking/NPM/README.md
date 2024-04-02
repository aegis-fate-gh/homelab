SSL certs come from Cloudflare, are of the Origin Server variety

To work in NPM, the .key file is modified. The beginning is changed to:
-----BEGIN RSA PRIVATE KEY-----

With the end changed to:
-----END RSA PRIVATE KEY-----

