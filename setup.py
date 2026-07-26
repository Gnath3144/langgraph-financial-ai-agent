from setuptools import setup, find_packages

setup(
    name="langgraph_financial_agent",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langgraph",
        "langchain",
        "pydantic"
    ],
)
