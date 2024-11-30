#include <stdio.h>
#include <stdlib.h>

#include "pocketpy.h"

int main(const int argc, const char **argv)
{
	if (argc != 2)
	{
		printf("Usage: %s <file>\n", argv[0]);
		return 1;
	}

	FILE *file = fopen(argv[1], "r");
	if (file == nullptr)
	{
		printf("Failed to open file: %s\n", argv[1]);
		return 1;
	}

	fseek(file, 0, SEEK_END);
	const long length = ftell(file);
	fseek(file, 0, SEEK_SET);

	char *buffer = malloc(length);
	if (buffer == nullptr)
	{
		printf("Failed to allocate memory for buffer\n");
		return 1;
	}

	fread(buffer, 1, length, file);

	py_initialize();
	const bool ok = py_exec(buffer, "<string>", EXEC_MODE, nullptr);

	if (!ok)
	{
		py_printexc();
	}

	fclose(file);
	free(buffer);
	py_finalize();

	return ok ? 0 : 1;
}
