# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kushagra/Desktop/Lab1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kushagra/Desktop/Lab1/build

# Include any dependencies generated for this target.
include CMakeFiles/Lab1.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Lab1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Lab1.dir/flags.make

CMakeFiles/Lab1.dir/main.cpp.o: CMakeFiles/Lab1.dir/flags.make
CMakeFiles/Lab1.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kushagra/Desktop/Lab1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Lab1.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Lab1.dir/main.cpp.o -c /home/kushagra/Desktop/Lab1/main.cpp

CMakeFiles/Lab1.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Lab1.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kushagra/Desktop/Lab1/main.cpp > CMakeFiles/Lab1.dir/main.cpp.i

CMakeFiles/Lab1.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Lab1.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kushagra/Desktop/Lab1/main.cpp -o CMakeFiles/Lab1.dir/main.cpp.s

CMakeFiles/Lab1.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/Lab1.dir/main.cpp.o.requires

CMakeFiles/Lab1.dir/main.cpp.o.provides: CMakeFiles/Lab1.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/Lab1.dir/build.make CMakeFiles/Lab1.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/Lab1.dir/main.cpp.o.provides

CMakeFiles/Lab1.dir/main.cpp.o.provides.build: CMakeFiles/Lab1.dir/main.cpp.o


CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o: CMakeFiles/Lab1.dir/flags.make
CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o: ../ext/glad/src/glad.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kushagra/Desktop/Lab1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o   -c /home/kushagra/Desktop/Lab1/ext/glad/src/glad.c

CMakeFiles/Lab1.dir/ext/glad/src/glad.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Lab1.dir/ext/glad/src/glad.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/kushagra/Desktop/Lab1/ext/glad/src/glad.c > CMakeFiles/Lab1.dir/ext/glad/src/glad.c.i

CMakeFiles/Lab1.dir/ext/glad/src/glad.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Lab1.dir/ext/glad/src/glad.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/kushagra/Desktop/Lab1/ext/glad/src/glad.c -o CMakeFiles/Lab1.dir/ext/glad/src/glad.c.s

CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o.requires:

.PHONY : CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o.requires

CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o.provides: CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o.requires
	$(MAKE) -f CMakeFiles/Lab1.dir/build.make CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o.provides.build
.PHONY : CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o.provides

CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o.provides.build: CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o


CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o: CMakeFiles/Lab1.dir/flags.make
CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o: ../ext/imgui/imgui.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kushagra/Desktop/Lab1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o -c /home/kushagra/Desktop/Lab1/ext/imgui/imgui.cpp

CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kushagra/Desktop/Lab1/ext/imgui/imgui.cpp > CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.i

CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kushagra/Desktop/Lab1/ext/imgui/imgui.cpp -o CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.s

CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o.requires:

.PHONY : CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o.requires

CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o.provides: CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o.requires
	$(MAKE) -f CMakeFiles/Lab1.dir/build.make CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o.provides.build
.PHONY : CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o.provides

CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o.provides.build: CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o


CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o: CMakeFiles/Lab1.dir/flags.make
CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o: ../ext/imgui/imgui_demo.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kushagra/Desktop/Lab1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o -c /home/kushagra/Desktop/Lab1/ext/imgui/imgui_demo.cpp

CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kushagra/Desktop/Lab1/ext/imgui/imgui_demo.cpp > CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.i

CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kushagra/Desktop/Lab1/ext/imgui/imgui_demo.cpp -o CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.s

CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o.requires:

.PHONY : CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o.requires

CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o.provides: CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o.requires
	$(MAKE) -f CMakeFiles/Lab1.dir/build.make CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o.provides.build
.PHONY : CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o.provides

CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o.provides.build: CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o


CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o: CMakeFiles/Lab1.dir/flags.make
CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o: ../ext/imgui/imgui_draw.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kushagra/Desktop/Lab1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o -c /home/kushagra/Desktop/Lab1/ext/imgui/imgui_draw.cpp

CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kushagra/Desktop/Lab1/ext/imgui/imgui_draw.cpp > CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.i

CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kushagra/Desktop/Lab1/ext/imgui/imgui_draw.cpp -o CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.s

CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o.requires:

.PHONY : CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o.requires

CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o.provides: CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o.requires
	$(MAKE) -f CMakeFiles/Lab1.dir/build.make CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o.provides.build
.PHONY : CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o.provides

CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o.provides.build: CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o


CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o: CMakeFiles/Lab1.dir/flags.make
CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o: ../ext/imgui/imgui_impl_glfw_gl3.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kushagra/Desktop/Lab1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o -c /home/kushagra/Desktop/Lab1/ext/imgui/imgui_impl_glfw_gl3.cpp

CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kushagra/Desktop/Lab1/ext/imgui/imgui_impl_glfw_gl3.cpp > CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.i

CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kushagra/Desktop/Lab1/ext/imgui/imgui_impl_glfw_gl3.cpp -o CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.s

CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o.requires:

.PHONY : CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o.requires

CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o.provides: CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o.requires
	$(MAKE) -f CMakeFiles/Lab1.dir/build.make CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o.provides.build
.PHONY : CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o.provides

CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o.provides.build: CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o


# Object files for target Lab1
Lab1_OBJECTS = \
"CMakeFiles/Lab1.dir/main.cpp.o" \
"CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o" \
"CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o" \
"CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o" \
"CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o" \
"CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o"

# External object files for target Lab1
Lab1_EXTERNAL_OBJECTS =

../bin/Lab1: CMakeFiles/Lab1.dir/main.cpp.o
../bin/Lab1: CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o
../bin/Lab1: CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o
../bin/Lab1: CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o
../bin/Lab1: CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o
../bin/Lab1: CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o
../bin/Lab1: CMakeFiles/Lab1.dir/build.make
../bin/Lab1: ext/glfw/src/libglfw3.a
../bin/Lab1: /usr/lib/x86_64-linux-gnu/librt.so
../bin/Lab1: /usr/lib/x86_64-linux-gnu/libm.so
../bin/Lab1: /usr/lib/x86_64-linux-gnu/libX11.so
../bin/Lab1: /usr/lib/x86_64-linux-gnu/libXrandr.so
../bin/Lab1: /usr/lib/x86_64-linux-gnu/libXinerama.so
../bin/Lab1: /usr/lib/x86_64-linux-gnu/libXcursor.so
../bin/Lab1: CMakeFiles/Lab1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kushagra/Desktop/Lab1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX executable ../bin/Lab1"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Lab1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Lab1.dir/build: ../bin/Lab1

.PHONY : CMakeFiles/Lab1.dir/build

CMakeFiles/Lab1.dir/requires: CMakeFiles/Lab1.dir/main.cpp.o.requires
CMakeFiles/Lab1.dir/requires: CMakeFiles/Lab1.dir/ext/glad/src/glad.c.o.requires
CMakeFiles/Lab1.dir/requires: CMakeFiles/Lab1.dir/ext/imgui/imgui.cpp.o.requires
CMakeFiles/Lab1.dir/requires: CMakeFiles/Lab1.dir/ext/imgui/imgui_demo.cpp.o.requires
CMakeFiles/Lab1.dir/requires: CMakeFiles/Lab1.dir/ext/imgui/imgui_draw.cpp.o.requires
CMakeFiles/Lab1.dir/requires: CMakeFiles/Lab1.dir/ext/imgui/imgui_impl_glfw_gl3.cpp.o.requires

.PHONY : CMakeFiles/Lab1.dir/requires

CMakeFiles/Lab1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Lab1.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Lab1.dir/clean

CMakeFiles/Lab1.dir/depend:
	cd /home/kushagra/Desktop/Lab1/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kushagra/Desktop/Lab1 /home/kushagra/Desktop/Lab1 /home/kushagra/Desktop/Lab1/build /home/kushagra/Desktop/Lab1/build /home/kushagra/Desktop/Lab1/build/CMakeFiles/Lab1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Lab1.dir/depend

