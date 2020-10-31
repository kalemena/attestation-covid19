#!/bin/bash

RESULT_PATH=${RESULT_PATH:-/data/}

make clean; make

mv attestation.pdf ${RESULT_PATH}
