# gRPC Python WellKnownTypes Bug

## Source
This example is taken from the official quickstart guide: https://grpc.io/docs/languages/python/quickstart/


## How to reproduce
Compile protofile with
```
python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. helloworld.proto
```

then run `greeter_server.py`and `greeter_client.py`.
