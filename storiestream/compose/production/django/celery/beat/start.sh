#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A storiestream.taskapp beat -l INFO
