from setuptools import find_packages, setup

# added to handle launch files
from glob import glob
import os

package_name = 'coh45_ex1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))) # added to handle launch files
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sree',
    maintainer_email='psreeram@gmail.com',
    description='Examples done in Rigbetellabs ROS2 program',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_1 = coh45_ex1.node1_pub:main',
            'node_2 = coh45_ex1.node2_sub_pub:main',
            'node_3 = coh45_ex1.node3_sub:main',
        ],
    },
)
