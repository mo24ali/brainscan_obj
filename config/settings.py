"""Centralized project settings loaded from the root .env file."""

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


def project_path(variable: str, default: str) -> Path:
    """Resolve a configured path relative to the project root."""
    value = Path(os.getenv(variable, default)).expanduser()
    return value if value.is_absolute() else PROJECT_ROOT / value


PROJECT_NAME = os.getenv("PROJECT_NAME", "BrainScan_AI")
RANDOM_STATE = int(os.getenv("RANDOM_STATE", "42"))

DATA_DIR = project_path("DATA_DIR", "data")
RAW_DATA_DIR = project_path("RAW_DATA_DIR", "data/raw")
PROCESSED_DATA_DIR = project_path("PROCESSED_DATA_DIR", "data/processed")
SPLITS_DIR = project_path("SPLITS_DIR", "data/splits")
EXTERNAL_DATA_DIR = project_path("EXTERNAL_DATA_DIR", "data/external")

NOTEBOOKS_DIR = project_path("NOTEBOOKS_DIR", "notebooks")
MODELS_DIR = project_path("MODELS_DIR", "models")
CLASSIFICATION_MODELS_DIR = project_path(
    "CLASSIFICATION_MODELS_DIR", "models/classification"
)
DETECTION_MODELS_DIR = project_path(
    "DETECTION_MODELS_DIR", "models/detection"
)
REPORTS_DIR = project_path("REPORTS_DIR", "reports")
FIGURES_DIR = project_path("FIGURES_DIR", "reports/figures")
METRICS_DIR = project_path("METRICS_DIR", "reports/metrics")
LOGS_DIR = project_path("LOGS_DIR", "logs")

MANIFEST_PATH = project_path("MANIFEST_PATH", "data/processed/manifest.csv")
TRAIN_MANIFEST_PATH = project_path("TRAIN_MANIFEST_PATH", "data/splits/train.csv")
VALIDATION_MANIFEST_PATH = project_path(
    "VALIDATION_MANIFEST_PATH", "data/splits/validation.csv"
)
TEST_MANIFEST_PATH = project_path("TEST_MANIFEST_PATH", "data/splits/test.csv")
SPLIT_SUMMARY_PATH = project_path(
    "SPLIT_SUMMARY_PATH", "data/splits/split_summary.json"
)

TRAIN_RATIO = float(os.getenv("TRAIN_RATIO", "0.70"))
VALIDATION_RATIO = float(os.getenv("VALIDATION_RATIO", "0.15"))
TEST_RATIO = float(os.getenv("TEST_RATIO", "0.15"))

IMAGE_SIZE = int(os.getenv("IMAGE_SIZE", "299"))
IMAGE_CHANNELS = int(os.getenv("IMAGE_CHANNELS", "3"))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "32"))
EPOCHS = int(os.getenv("EPOCHS", "30"))
LEARNING_RATE = float(os.getenv("LEARNING_RATE", "0.001"))
NUM_WORKERS = int(os.getenv("NUM_WORKERS", "4"))

YOLO_MODEL = os.getenv("YOLO_MODEL", "yolov8n.pt")
YOLO_IMAGE_SIZE = int(os.getenv("YOLO_IMAGE_SIZE", "640"))
YOLO_EPOCHS = int(os.getenv("YOLO_EPOCHS", "50"))

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
STREAMLIT_PORT = int(os.getenv("STREAMLIT_PORT", "8501"))

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "./mlruns")

if not abs(TRAIN_RATIO + VALIDATION_RATIO + TEST_RATIO - 1.0) < 1e-9:
    raise ValueError("TRAIN_RATIO + VALIDATION_RATIO + TEST_RATIO must equal 1.")
