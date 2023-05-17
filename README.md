



**Add dependency**
```shell
## Add runtime dependency
poery add boto3

## Add development dependency
poetry add pytest -G dev
```

**Run main**
```shell
poetry export -f requirements.txt --output requirements.txt
```
**Run tests**
```shell
poetry run pytest
```