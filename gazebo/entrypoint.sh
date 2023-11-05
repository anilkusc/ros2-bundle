#!/bin/bash
set -xe
gzserver --verbose &
gz model --model-name $WORLD_NAME --spawn-file "$WORLD_NAME".sdf
sleep infinity