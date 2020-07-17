import platform
from setuptools import setup, find_packages

PLATFORM = platform.system()

REQUIREMENTS = [
  'numpy',
  'pillow',
  'pycocotools-windows' if 'Windows' in PLATFORM else 'wf-pycocotools',
  'torch',
  'torchvision'
]

setup(
  name = 'torchvision-detection',
  version = '0.6.5',
  description = 'Object detection reference training scripts.',
  author = 'PyTorch Team',
  maintainer = 'Danilo Peixoto',
  maintainer_email = 'danilopeixoto@outlook.com',
  license = 'BSD',
  url = 'https://github.com/danilopeixoto/torchvision-detection',
  download_url = 'https://github.com/danilopeixoto/torchvision-detection/archive/v0.6.5.tar.gz',
  packages = find_packages(),
  python_requires = '>=3.6',
  install_requires = REQUIREMENTS,
  zip_safe = False)
