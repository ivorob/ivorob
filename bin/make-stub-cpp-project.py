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
"""

with open(os.path.join(args.path, "CMakeLists.txt"), 'w') as file:
    file.write(cmakeFileContent.replace('{project}', args.project))

sourceDirectory = os.path.join(args.path, 'src')
os.mkdir(sourceDirectory)

mainCppFileContent = """#include <iostream>

int main(int /* argc */, char* /* argv */[]) {
    std::cout << "{project}" << std::endl;
    return 0;
}
"""

with open(os.path.join(sourceDirectory, 'main.cpp'), 'w') as file:
    file.write(mainCppFileContent.replace('{project}', args.project))
    
