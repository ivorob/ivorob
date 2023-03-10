#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('project')
args = parser.parse_args()

os.mkdir(args.path)

cmakeFileContent = """CMAKE_MINIMUM_REQUIRED (VERSION 3.0)
PROJECT ({project})

SET (SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
SET (INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)

SET (CMAKE_CXX_STANDARD 17)

SET (SOURCES 
        ${SRC_DIR}/main.cpp
    )

ADD_EXECUTABLE ({project} ${SOURCES})
TARGET_INCLUDE_DIRECTORIES ({project} PRIVATE ${INCLUDE_DIR})
"""

with open(os.path.join(args.path, "CMakeLists.txt"), 'w') as file:
    file.write(cmakeFileContent.replace('{project}', args.project))

sourceDirectory = os.path.join(args.path, 'src')
os.mkdir(sourceDirectory)

mainCppFileContent = """#include <iostream>

#include "DebugHelpers.h"

int main() {
    std::cout << "{project}" << std::endl;
    return 0;
}
"""

with open(os.path.join(sourceDirectory, 'main.cpp'), 'w') as file:
    file.write(mainCppFileContent.replace('{project}', args.project))

includeDirectory = os.path.join(args.path, 'include')
os.mkdir(includeDirectory)

helpersFileContent = """#pragma once

#include <ostream>

// print vector
template <typename T>
std::ostream& operator<<(std::ostream& output, const std::vector<T>& data) {
    output << "[";
    for (size_t i = 0; i < data.size(); ++i) {
        if (i != 0) {
            output << ", ";
        }

        output << data[i];
    }

    output << "]";
    return output;
}

"""
    
with open(os.path.join(includeDirectory, 'DebugHelpers.h'), 'w') as file:
    file.write(helpersFileContent)
