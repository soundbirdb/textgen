# textgen

A fork of [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) — a Gradio web UI for running Large Language Models.

## Features

- Supports multiple model backends: transformers, llama.cpp, ExLlamaV2, AutoGPTQ, AutoAWQ, and more
- LoRA loading and training (including QLoRA)
- Multimodal support (images, documents)
- Extensions API for custom functionality
- OpenAI-compatible API server
- Character-based chat with persona support
- Notebook and instruct modes

## Installation

### One-click installers (recommended)

Download the latest portable release from the [Releases](../../releases) page for your platform:

- `textgen-cuda-*.zip` — NVIDIA GPU (CUDA)
- `textgen-ik-cuda-*.zip` — NVIDIA GPU with IK CUDA extensions
- `textgen-ik-*.zip` — CPU / other

Extract the archive and run `start_windows.bat` (Windows) or `start_linux.sh` (Linux) or `start_macos.sh` (macOS).

### Manual installation

**Prerequisites:** Python 3.11, Git

```bash
git clone https://github.com/your-org/textgen
cd textgen

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### GPU-specific requirements

| Backend | Install command |
|---|---|
| NVIDIA CUDA | `pip install -r requirements_cuda.txt` |
| AMD ROCm | `pip install -r requirements_rocm.txt` |
| CPU only | `pip install -r requirements_cpu.txt` |

## Usage

```bash
python server.py
```

Then open your browser at `http://127.0.0.1:7860`.

### Common flags

| Flag | Description |
|---|---|
| `--model MODEL` | Load a model at startup |
| `--listen` | Listen on all network interfaces |
| `--port PORT` | Set the port (default: 7860) |
| `--api` | Enable the OpenAI-compatible API |
| `--api-port PORT` | Set the API port (default: 5000) |
| `--share` | Create a public Gradio link |
| `--cpu` | Force CPU inference |
| `--load-in-4bit` | Load model in 4-bit quantization |
| `--load-in-8bit` | Load model in 8-bit quantization |
| `--n-gpu-layers N` | Number of layers to offload to GPU (llama.cpp) |

For the full list of options run:

```bash
python server.py --help
```

### My personal startup command

I typically run this on my local machine with a llama.cpp model and the API enabled:

```bash
python server.py --model models/mistral-7b-instruct.Q4_K_M.gguf --n-gpu-layers 28 --api
```

## Contributing

Pull requests are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and use the provided PR template.

For bugs, use the [bug report template](.github/ISSUE_TEMPLATE/bug_report_template.yml).  
For feature ideas, use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md).

## License

This project is licensed under the [AGPL-3.0 License](LICENSE).
