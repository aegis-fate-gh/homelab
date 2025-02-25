Loki Logging

Non GPU Node:
{
  "log-driver": "loki",
    "log-opts": {
        "loki-url": "http://192.168.6.7:3100/loki/api/v1/push",
        "loki-batch-size": "400",
        "max-size": "100m",
        "loki-retries": "5",
        "loki-max-backoff": "10s"
    }
}

GPU Nodes:
{
  "log-driver": "loki",
    "log-opts": {
        "loki-url": "http://192.168.6.7:3100/loki/api/v1/push",
        "loki-batch-size": "400",
        "max-size": "100m",
        "loki-retries": "5",
        "loki-max-backoff": "10s"
    },
  "runtimes": {
    "nvidia": {
      "path": "/usr/bin/nvidia-container-runtime",
      "runtimeArgs": []
    }
  },
  "default-runtime": "nvidia",
  "node-generic-resources": [
    "NVIDIA-GPU=GPU-6f43d74b"
    ]
}