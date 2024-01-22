import setuptools

setuptools.setup(
    name="TesterCli",
    version="1.0.0",
    packages=setuptools.find_packages(),
    py_modules=['main', 'cli'],
    install_requires=[
        "Faker>=22.4.0",
        "requests>=2.31.0",
        "typer>=0.9.0",
        "pyperclip>=1.8.2",
    ],
    entry_points={
        "console_scripts": ["TesterCli=main:app"]
    }
)
