# Compiler and flags
CXX = g++-11
CXXFLAGS = -Wall -Wextra -O3 -march=native -Iinclude -I/usr/include/eigen3
LDFLAGS = -fopenmp

# Targets
TARGETS = \
    bin/parallel \
    bin/a_plate_with_constant_V \
    bin/parallel_cap_cv \
    bin/parallel_cap_dv \
    bin/parallel_cap_hole \
    bin/parallel_cap_dv_with_float

# Default build all
all: $(TARGETS)

bin/parallel: src/parallel.cpp
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)

bin/a_plate_with_constant_V: src/a_plate_with_constant_V.cpp
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)

bin/parallel_cap_cv: src/parallel_cap_cv.cpp
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)

bin/parallel_cap_dv: src/parallel_cap_dv.cpp
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)

bin/parallel_cap_hole: src/parallel_cap_hole.cpp
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)

bin/parallel_cap_dv_with_float: src/parallel_cap_dv_with_float.cpp
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)

# Clean
clean:
	rm -rf bin/*

.PHONY: all clean
