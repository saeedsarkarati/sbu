#!/usr/bin/env python3

import os
import argparse

def generate_makefile(src_dir='src', bin_dir='bin', eigen_path='/usr/include/eigen3'):
    # List of targets in order
    targets_order = [
        'parallel',
        'a_plate_with_constant_V',
        'parallel_cap_cv',
        'parallel_cap_dv',
        'parallel_cap_dv_with_float'
    ]
    
    # Check which source files exist
    existing_targets = []
    missing_sources = []
    
    for target in targets_order:
        src_file = os.path.join(src_dir, f"{target}.cpp")
        if os.path.exists(src_file):
            existing_targets.append(target)
        else:
            missing_sources.append(src_file)
    
    # Build TARGETS section with correct formatting (all lines ending with backslash)
    targets_section = "# Targets\nTARGETS = \\\n"
    targets_section += " \\\n".join([f"    {bin_dir}/{target}" for target in existing_targets]) + "\n"

    # Build complete Makefile content
    makefile_lines = [
        "# Compiler and flags",
        "CXX = g++",
        f"CXXFLAGS = -Wall -Wextra -O3 -march=native -fopenmp -Iinclude -I{eigen_path}",
        "LDFLAGS = -fopenmp",
        "",
        targets_section,
        "# Default build all",
        "all: $(TARGETS)",
        ""
    ]

    # Add build rules for each target
    for target in existing_targets:
        makefile_lines.extend([
            f"{bin_dir}/{target}: {src_dir}/{target}.cpp",
            "\t@mkdir -p bin",  # Actual tab character
            "\t$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)",  # Actual tab character
            ""
        ])

    # Add clean rule
    makefile_lines.extend([
        "# Clean",
        "clean:",
        "\trm -rf bin/*",  # Actual tab character
        "",
        ".PHONY: all clean"
    ])

    # Write Makefile
    with open('Makefile', 'w') as f:
        f.write("\n".join(makefile_lines))
    
    # Print summary
    print(f"Successfully generated Makefile with {len(existing_targets)} targets:")
    for target in existing_targets:
        print(f" - {bin_dir}/{target}")

    if missing_sources:
        print("\nWarning: Skipped targets due to missing sources:")
        for target in set(targets_order) - set(existing_targets):
            print(f" - {target}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automatically generate Makefile')
    parser.add_argument('--src', default='src', help='Source directory (default: src)')
    parser.add_argument('--bin', default='bin', help='Output directory (default: bin)')
    parser.add_argument('--eigen', default='/usr/include/eigen3', 
                      help='Eigen library path (default: /usr/include/eigen3)')
    
    args = parser.parse_args()
    generate_makefile(args.src, args.bin, args.eigen)
