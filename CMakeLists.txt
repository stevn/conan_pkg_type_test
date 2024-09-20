set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN 1)

project(stuff_prj)

include(CTest)
include(GenerateExportHeader)

add_subdirectory(src/lib/stuff)
add_subdirectory(src/app/stufftool)
