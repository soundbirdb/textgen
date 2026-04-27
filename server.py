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
    parser.add_argument('--threads', type=int, default=0,
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
    parser.add_argument('--listen-host', type=str, default='0.0.0.0',
                        help='Host to listen on when --listen is used')
    parser.add_argument('--share', action='store_true',
                        help='Create a public Gradio share link')
    parser.add_argument('--auto-launch', action='store_true', default=True,
                        help='Open the web UI in the default browser on startup')
    parser.add_argument('--gradio-auth', type=str, default=None,
                        help='Gradio authentication in format username:password')
    parser.add_argument('--api', action='store_true',
                        help='Enable the API extension')
    parser.add_argument('--api-port', type=int, default=5000,
                        help='Port for the API server')
    parser.add_argument('--api-key', type=str, default='',
                        help='API key for authentication')
    parser.add_argument('--public-api', action='store_true',
                        help='Create a public Gradio share link for the API')

    # UI arguments
    parser.add_argument('--chat', action='store_true',
                        help='Launch in chat mode by default')
    parser.add_argument('--notebook', action='store_true',
                        help='Launch in notebook mode by default')
    parser.add_argument('--extensions', type=str, nargs='+', default=None,
                        help='Extensions to load at startup')
    parser.add_argument('--verbose', action='store_true',
                        help='Enable verbose logging output')

    return parser.parse_args()


def check_requirements():
    """
    Check that required dependencies are available.
    """
    try:
        import torch
        logger.info(f'PyTorch version: {torch.__version__}')
        if torch.cuda.is_available():
            logger.info(f'CUDA available: {torch.cuda.get_device_name(0)}')
        else:
            logger.warning('CUDA not available, running on CPU')
    except ImportError:
        logger.error('PyTorch is not installed. Please install it before running.')
        sys.exit(1)

    try:
        import gradio
        logger.info(f'Gradio version: {gradio.__version__}')
    except ImportError:
        logger.error('Gradio is not installed. Please run: pip install gradio')
        sys.exit(1)


def main():
    """
    Main entry point for the TextGen server.
    """
    args = parse_arguments()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    logger.info('Starting TextGen Web UI...')
    check_requirements()

    # Ensure required directories exist
    for directory in ['models', 'loras', 'characters', 'presets', 'prompts', 'extensions', 'logs']:
        os.makedirs(directory, exist_ok=True)

    logger.info(f'Model directory: {args.model_dir}')
    if args.model:
        logger.info(f'Loading model: {args.model}')

    # TODO: Initialize the UI and model loader
    # This will be expanded as modules are added
    logger.info('Server initialization complete.')


if __name__ == '__main__':
    main()
