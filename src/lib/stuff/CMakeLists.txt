add_library(stuff)

generate_export_header(stuff)

target_sources(stuff
    PRIVATE
        include/stuff.h
        ${CMAKE_CURRENT_BINARY_DIR}/stuff_export.h
        stuff.cpp
)
target_include_directories(stuff
    PUBLIC
        include
        ${CMAKE_CURRENT_BINARY_DIR}  # Header file "stuff_export.h" is generated in current binary dir.
)
target_compile_definitions(stuff
    PRIVATE
        stuff_EXPORTS
)
