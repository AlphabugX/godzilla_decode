# Godzilla_Deocde
## 哥斯拉JSP和java内存马 全流量解密脚本
```bash
pip install Crypto
```
or
安装Anaconda

```python
usage: Godzilla.py [-h] [-k KEY] [-m MODE] -d DATA
Godzilla.py: error: the following arguments are required: -d/--data
```
食用方法
```bash
python Godzilla.py -d 38F3ABE85948D564vfBIMcn2xlCZeTt3xKajRhv1UfDC5+KidKVHQV0TYeGnxL/CeXkYbegPI6tkcWYJnH10tRkuF/r0Z57m6xDziNeUjCtB8WEpN7K8wpQZmbwQvzA4JYKxQLfwVcZK6wO0U3oV1/JtcS+
gBy7sFYq64K8hIoJZKXvF73ZSdcTNTNvGcnfeW7CWHuhQanjKoEVdescpdva1QVbxxLAiLTvjgquWISTy9ycQCqpi8DTgHRo=D7028F042ACDF2CA



code
```python
    alphabug = argparse.ArgumentParser(description="Godzilla Jsp Decoder,\tAuthor:Alphabug@RedTeam.site")
    alphabug.add_argument("-k","--key",help="Domain,For example: -k 3c6e0b8a9c15224a (Default:3c6e0b8a9c15224a)",default="3c6e0b8a9c15224a")
    alphabug.add_argument("-m","--mode",help="Email ,For example: -m post -d post_data | -m data -d return_data (Default:return_data)",default="return_data")
    alphabug.add_argument("-d","--data",help="Email ,For example: -m post -d 0mQU%2BS1pFnTz3ttVTnAgJf4rvU9E3tQySxwinpW%2F0fDyiB6qieU72U9P3PIb3i45CpP2Y9BsSVqc%2FVY2umWLyBCh%2F%2FphkKaNbf7RCjD4mzY%3D \n-m data -d 38F3ABE85948D564vfBIMcn2xlCZeTt3xKajRhv1UfDC5+KidKVHQV0TYeGnxL/CeXkYbegPI6tkcWYJnH10tRkuF/r0Z57m6xDziNeUjCtB8WEpN7K8wpQZmbwQvzA4JYKxQLfwVcZK6wO0U3oV1/JtcS+gBy7sFYq64K8hIoJZKXvF73ZSdcTNTNvGcnfeW7CWHuhQanjKoEVdescpdva1QVbxxLAiLTvjgquWISTy9ycQCqpi8DTgHRo=D7028F042ACDF2CA",required = True)
    args = alphabug.parse_args()
```
