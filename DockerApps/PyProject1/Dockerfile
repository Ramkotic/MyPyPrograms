FROM ubuntu:2404
RUN sudo apt update -y
RUN sudo apt install python3.8.6 -y
RUN mkdir -p /u01/middleware
COPY ./file_name_with_size_based_on_extensions_info.py /u01/middleware
CMD ["python.exe", "file_name_with_size_based_on_extensions_info.py"]
