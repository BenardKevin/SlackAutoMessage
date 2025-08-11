import subprocess
import sys

MIN_PYTHON = (3, 8)
REQUIRED_PACKAGES = ["setuptools", "streamlit", "slack_sdk", "python-dotenv"]

def check_python_version():
    if sys.version_info < MIN_PYTHON:
        sys.stderr.write(f"Error: Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or higher is required.\n")
        sys.exit(1)

def install_package(package):
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_packages():
    try:
        import pkg_resources
    except ImportError:
        print("Installing setuptools (required for pkg_resources)...")
        install_package("setuptools")
        import pkg_resources

    installed = {pkg.key for pkg in pkg_resources.working_set}
    for package in REQUIRED_PACKAGES:
        if package not in installed:
            install_package(package)
        else:
            print(f"{package} already installed.")

if __name__ == "__main__":
    print("Checking Python environment...")
    check_python_version()
    check_and_install_packages()
    print("\nSetup complete.")
