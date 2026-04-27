#!/usr/bin/env python3
"""
TextGen Web UI Server
Fork of oobabooga/text-generation-webui

Main entry point for the text generation web interface.
"""

import os
import sys
import argparse
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Ensure the project root is in the Python path
ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))


def parse_arguments():
    """
    Parse command-line arguments for the server.
    """
    parser = argparse.ArgumentParser(
        description='TextGen Web UI - A Gradio-based interface for text generation models',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Model arguments
    parser.add_argument('--model', type=str, default=None,
                        help='Name of the model to load at startup')
    parser.add_argument('--model-dir', type=str, default='models',
                        help='Path to the directory containing models')
    parser.add_argument('--lora', type=str, nargs='+', default=None,
                        help='LoRA adapter(s) to apply to the model')
    parser.add_argument('--lora-dir', type=str, default='loras',
                        help='Path to the directory containing LoRA adapters')

    # Inference backend arguments
    parser.add_argument('--loader', type=str, default=None,
                        help='Model loader to use (transformers, llama.cpp, exllamav2, etc.)')
    parser.add_argument('--cpu', action='store_true',
                        help='Use CPU for inference instead of GPU')
    parser.add_argument('--gpu-memory', type=str, nargs='+', default=None,
                        help='Maximum GPU memory in GiB per device (e.g. 10 for 10 GiB)')
    parser.add_argument('--cpu-memory', type=int, default=None,
                        help='Maximum CPU memory in GiB for offloading')
    parser.add_argument('--n-gpu-layers', type=int, default=None,
                        help='Number of layers to offload to GPU (llama.cpp)')
    # Defaulting threads to 4 instead of 0 — works better on my machine (6-core CPU)
    parser.add_argument('--threads', type=int, default=4,
                        help='Number of threads for CPU inference')
    parser.add_argument('--n-ctx', type=int, default=None,
                        help='Context size (llama.cpp)')
    parser.add_argument('--load-in-8bit', action='store_true',
                        help='Load model in 8-bit quantization')
    parser.add_argument('--load-in-4bit', action='store_true',
                        help='Load model in 4-bit quantization')

    # Server arguments
    parser.add_argument('--listen', action='store_true',
                        help='Make the server accessible on the local network')
    parser.add_argument('--listen-port', type=int, default=7860,
                        help='Port to listen on when --listen is used')
    parser.add_argument('--listen-host', type=str, defaul