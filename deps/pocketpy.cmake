include(FetchContent)

FetchContent_Declare(pocketpy
	GIT_REPOSITORY https://github.com/pocketpy/pocketpy.git
	GIT_TAG v2.0.2
)

message(STATUS "Downloading: pocketpy")
FetchContent_MakeAvailable(pocketpy)