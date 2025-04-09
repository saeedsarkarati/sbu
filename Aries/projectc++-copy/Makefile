# Compiler settings
CXX = g++
CXXFLAGS = -Wall -Wextra -O3 -march=native -fopenmp -Iinclude -I/usr/include/eigen3
LDFLAGS = -fopenmp

# Source files
SRCS = \
    src/a_plate_with_constant_V.cpp \
    src/parallel_cap_cv.cpp \
    src/parallel_cap_dv.cpp \
    src/parallel_cap_dv_with_float.cpp \
    src/tiles.cpp

# Object files
OBJS = $(patsubst src/%.cpp,obj/%.o,$(SRCS))

# Targets
TARGETS = $(patsubst src/%.cpp,bin/%,$(filter-out src/tiles.cpp,$(SRCS)))

# Directory structure
DIRS = bin obj

# Main targets
all: $(DIRS) $(TARGETS)

# Rule to build executables
bin/%: obj/%.o obj/tiles.o
	@echo "Building $@"
	$(CXX) $(LDFLAGS) $^ -o $@

# Rule to compile source files
obj/%.o: src/%.cpp
	@echo "Compiling $<"
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Create directories
$(DIRS):
	@mkdir -p $@

# Clean
clean:
	@echo "Cleaning build files..."
	@rm -rf bin obj

.PHONY: all clean

# Dependency rules (generated automatically or manually)
obj/tiles.o: src/tiles.cpp include/tiles.h
obj/parallel.o: src/parallel.cpp include/tiles.h
obj/a_plate_with_constant_V.o: src/a_plate_with_constant_V.cpp include/tiles.h
obj/parallel_cap_cv.o: src/parallel_cap_cv.cpp include/tiles.h
obj/parallel_cap_dv.o: src/parallel_cap_dv.cpp include/tiles.h
obj/parallel_cap_dv_with_float.o: src/parallel_cap_dv_with_float.cpp include/tiles.h
