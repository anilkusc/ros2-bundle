#!/bin/bash
set -xe
gzserver --verbose &
gz model --model-name double_pendulum --spawn-file double_pendulum.sdf
sleep infinity