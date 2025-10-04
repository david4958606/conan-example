build:
	conan build . --build=missing -pr=clang -s build_type=Debug
release:
	conan build . --build=missing -pr=clang -s build_type=Release
install:
	conan install . --build=missing -pr=clang -s build_type=Debug
install-release:
	conan install . --build=missing -pr=clang -s build_type=Release
clean:
	if exist build rmdir /s /q build
	if exist bin rmdir /s /q bin
	if exist lib rmdir /s /q lib
	if exist CMakeUserPresets.json del /q CMakeUserPresets.json
.PHONY: build release install install-release clean