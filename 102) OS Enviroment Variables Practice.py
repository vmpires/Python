import os

## 2 ways of getting path OS Variables
OS = os.environ.get("OS")
Processor = os.environ["PROCESSOR_ARCHITECTURE"]

## Setting OS Variables
os.environ["MY_VARIABLE"] = "ThisIsMine"

print(OS)
print(Processor)
print(os.environ["MY_VARIABLE"])