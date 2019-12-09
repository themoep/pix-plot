from setuptools import setup
from os.path import join
import os

# populate list of all paths in `./pixplot/web`
web = []
for root, subdirs, files in os.walk(os.path.join('pixplot', 'web')):
  if not files: continue
  for file in files:
    web.append(os.path.join(root.replace('pixplot/', ''), file))

setup(
  name='pixplot',
  version='0.0.28',
  packages=['pixplot'],
  package_data={
    'pixplot': web,
  },
  keywords = ['computer-vision', 'webgl', 'three.js', 'tensorflow', 'machine-learning'],
  description='Visualize large image collections with WebGL',
  url='https://github.com/yaledhlab/pix-plot',
  author='Douglas Duhaime',
  author_email='douglas.duhaime@gmail.com',
  license='MIT',
  install_requires=[
    'glob2>=0.6',
    'Keras>=2.3.0',
    'Pillow>=6.1.0',
    'numpy>=1.16.0',
    'scikit-learn>=0.19.0',
    'tensorflow>=1.14.0,<=2.0.0',
    'umap-learn>=0.3.10',
    'yale-dhlab-rasterfairy>=1.0.3',
    'yale-dhlab-keras-preprocessing>=1.1.1',
    'ImageHash>=4.0',
  ],
  entry_points={
    'console_scripts': [
      'pixplot=pixplot:parse',
    ],
  },
)
