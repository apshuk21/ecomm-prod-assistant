import importlib.metadata

packages = ["langchain", "langchain-core", "python-dotenv", "ipykernel", "streamlit"]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} not installed")
