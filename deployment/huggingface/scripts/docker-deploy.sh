#!/bin/bash

# Copyright 2026 Ankur Sinha
# Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
# File:  docker/deploy.sh
#
# Script for docker deployments


# currently unused
#echo "Re-starting MCP server"
#nml-mcp &

echo "Starting fastapi"
fastapi run neuroml_ai/neuroml_ai/api/main.py --port 8005 &

echo "Starting streamlit frontend"
streamlit run neuroml_ai/neuroml_ai/ui/streamlit_ui.py --server.port=7860 --server.address=0.0.0.0
