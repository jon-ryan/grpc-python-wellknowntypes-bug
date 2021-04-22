# gRPC Python WellKnownTypes Bug

## How to reproduce
Compile protofile with
```
python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. helloworld.proto
```

then run `greeter_server.py`and `greeter_client.py`.
