cmake_minimum_required(VERSION 3.7)
set(AssignmentNameHere practice1)
project(${AssignmentNameHere})

set(CMAKE_CXX_STANDARD 11)

file(GLOB DEPS_SOURCES ext/glad/src/glad.c)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY  ${PROJECT_SOURCE_DIR}/bin)
include_directories("ext/glm/"
        "ext/glfw/include"
        "ext/glad/include"
        "ext/imgui"
        )



option(GLFW_BUILD_DOCS OFF)
option(GLFW_BUILD_EXAMPLES OFF)
option(GLFW_BUILD_TESTS OFF)
add_subdirectory(ext/glfw)


file(GLOB IMGUI_SOURCE
        ext/imgui/*.cpp
        ext/imgui/*.h
        )


set(PLATFORM_LINK )
if (UNIX)
    set(PLATFORM_LINK -ldl)
endif (UNIX)


set(SOURCE_FILES main.cpp)
add_executable(${AssignmentNameHere} ${SOURCE_FILES}  ${DEPS_SOURCES} ${IMGUI_SOURCE})
target_link_libraries(${AssignmentNameHere} glfw ${GLFW_LIBRARIES} ${PLATFORM_LINK} )
