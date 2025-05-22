from setuptools import setup, find_packages

setup(
    name='tasks_dags',
    version='0.1.0',
    description='Pacote com tasks e logger para Airflow',
    author='Seu Nome',
    author_email='seu.email@exemplo.com',
    packages=find_packages(where='src'),   # find packages inside src/
    package_dir={'': 'src'},                # source directory
    install_requires=[
        # Add any project dependencies here
    ],
    python_requires='>=3.7',
)
