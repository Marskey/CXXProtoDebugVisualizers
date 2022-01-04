cmake_minimum_required(VERSION 3.16)
project(test_lldb_var_format)

set(CMAKE_CXX_STANDARD 17)

find_package(Protobuf REQUIRED)
include_directories(${Protobuf_INCLUDE_DIRS})
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS test.proto)
add_executable(test_lldb_var_format main.cpp ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(test_lldb_var_format ${Protobuf_LIBRARIES})