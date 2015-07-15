#!/bin/bash
set -e
rm -rf ./hieradata
rm -rf ./environments
r10k deploy environment -p -c r10k.yaml
