cmake_minimum_required(VERSION 3.30)
project(aoc2024 LANGUAGES C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(aoc2024 main.c)

include(deps/pocketpy.cmake)

target_link_libraries(${PROJECT_NAME} PRIVATE pocketpy)

target_include_directories(${PROJECT_NAME} PRIVATE
	"${pocketpy_SOURCE_DIR}/include"
)