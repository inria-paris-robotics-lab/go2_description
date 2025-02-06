# Install init file
python_install_on_site(${PROJECT_NAME} __init__.py)

# Populate the path file and install it manually
configure_file(${PROJECT_NAME}/path.py.in ${PROJECT_NAME}/path.py)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}/path.py
        DESTINATION "${PYTHON_SITELIB}/${PROJECT_NAME}")