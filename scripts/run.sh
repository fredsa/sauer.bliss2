#!/bin/bash
#
set -uev

/fred/lib/sdk193vmruntime/dev_appserver.py . \
  --api_host=0.0.0.0 \
  --api_port=51001  \
  --skip_sdk_update_check \
  --docker_daemon_url=tcp://localhost:4243
